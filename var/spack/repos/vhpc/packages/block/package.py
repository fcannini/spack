# SPDX-License-Identifier: (Apache-2.0 OR MIT)
# Author Fabricio Cannini <fcanniniREMOVETHISOBVIOUSPLACEHOLDER ANOTHEROBVIOUSPLACEHOLDER gmail.com>
# Copyright 2019- Fabricio Cannini

from spack import *


class Block(MakefilePackage):
    """
    BLOCK implements the density matrix renormalization group (DMRG) algorithm for quantum chemistry.
    The DMRG is a variational wavefunction method.
    Compared to other quantum chemical methods, it efficiently describes strong,
    multi-reference correlation in a large number of active orbitals (occupancies far from 0 or 2).
    The method is also provably optimal for correlation with a one-dimensional topology, that is,
    where orbitals are arranged with a chain- or ring-like connectivity.
    """

    homepage = "https://sanshar.github.io/Block"
    url      = "http://www.sunqm.net/pyscf/files/src/block-1.5.3.tar.gz"

    version('1.5.3', sha256='0f8f97f3983f7b938d94470732884cd28e08589dd116a2e0b3dc62664a0b91d9') # noqa

    variant('mpi', default=True, description='MPI-enabled build')

    depends_on('blas')
    depends_on('lapack')
    depends_on('mpi')
    # https://sanshar.github.io/Block/build.html
    depends_on('boost@1.56.0 +mpi +taggedlayout ~fiber cxxstd=11',
            patches=[
                patch(
                    'https://sf.net/projects/mancha/files/misc/boost-1.56.0_copy_file.diff', # noqa
                    when='@1.56.0',
                    sha256='e3ab2a66041cc309fe164de7c06c2b4a82e91eed6076540a480705966968a194'), # noqa
                patch(
                    'https://patch-diff.githubusercontent.com/raw/boostorg/serialization/pull/3.patch', # noqa
                    level=2,
                    when='@1.56.0',
                    sha256='b2680e3f4090bd7b09e9ebdd36d13baa7c8caa24c192484bd2b5452d43a523b3') # noqa
            ]
    )

    def edit(self, spec, prefix):
        spec = self.spec

        makefile = FileFilter('Makefile')
        makefile.filter('USE_BOOST56\s+=.*$', 'USE_BOOST56 = yes')
        makefile.filter('BOOSTINCLUDE\s+=.*$', 'BOOSTINCLUDE = '\
                + spec['boost'].headers.cpp_flags)
        makefile.filter('BOOSTLIB\s+=.*$', 'BOOSTLIB = -L' \
                + spec['boost'].prefix.lib \
                + ' -lboost_serialization-mt\
                -lboost_filesystem-mt\
                -lboost_system-mt -lrt')
        makefile.filter('LAPACKBLAS\s+=.*$', 'LAPACKBLAS = '\
                + spec['blas'].libs.ld_flags)

        if '+mpi' in spec:
            makefile.filter('CXX\s+=.*$', 'CXX = ' + spec['mpi'].mpicxx)
            makefile.filter('MPICXX\s+=.*$', 'MPICXX = ' + spec['mpi'].mpicxx)
            makefile.filter('USE_MPI\s+=.*$', 'USE_MPI = yes')
            makefile.filter('MPI_LIB\s+=.*$', 'MPI_LIB = -lboost_mpi-mt')
        else:
            makefile.filter('CXX\s+=.*$', 'CXX = c++')

    def build(self, spec, prefix):
        make()

    def install(self, spec, prefix):
        mkdirp(self.prefix.bin)
        install('block.spin_adapted', self.prefix.bin)

   #@run_after('install')
   #def post_install(self):
   #    return
