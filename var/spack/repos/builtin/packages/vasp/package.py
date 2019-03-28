# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os


class Vasp(MakefilePackage):
    """
    The Vienna Ab initio Simulation Package (VASP)
    is a computer program for atomic scale materials modelling,
    e.g. electronic structure calculations
    and quantum-mechanical molecular dynamics, from first principles.
    """

    homepage = "http://vasp.at"
    url      = "file://{0}/vasp.5.4.4.tar.gz".format(os.getcwd())

    version('5.4.4', sha256='5bd2449462386f01e575f9adf629c08cb03a13142806ffb6a71309ca4431cfb3') # noqa

    depends_on('blas')
    depends_on('lapack')
    depends_on('fftw')
    depends_on('mpi')
    depends_on('netlib-scalapack')

    parallel = False

    def edit(self, spec, prefix):
        spec = self.spec

        if '%gcc' in spec:
            make_include = join_path('arch', 'makefile.include.linux_gnu')
        else:
            make_include = join_path('arch', 'makefile.include.linux_'
                                     + spec.compiler.name)

        os.rename(make_include, 'makefile.include')
        make_include = FileFilter('makefile.include')

        make_include.filter('^LIBDIR[ ]+=.*$', '')

        make_include.filter('^BLAS[ ]+=.*$', 'BLAS\t\t= '
                            + spec['blas'].libs.ld_flags)

        make_include.filter('^LAPACK[ ]+=.*$', 'LAPACt\t\t= '
                            + spec['lapack'].libs.ld_flags)

        make_include.filter('^FFTW[ ]+.*$', 'FFTW\t\t= '
                            + spec['fftw'].prefix)

        make_include.filter('^MPI_INC[ ]+=.*$', 'MPI_INC\t\t= '
                            + spec['mpi'].prefix.include)

        make_include.filter('^SCALAPACK[ ]+=.*$', 'SCALAPACK\t= '
                            + spec['netlib-scalapack'].libs.ld_flags)

    def build(self, spec, prefix):
        make()

    def install(self, spec, prefix):
        mkdirp(self.prefix.bin)
        install_tree('bin/', self.prefix.bin)
