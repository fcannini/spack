# SPDX-License-Identifier: (Apache-2.0 OR MIT)
#
# Author Fabricio Cannini <fcanniniREMOVETHISOBVIOUSPLACEHOLDER ANOTHEROBVIOUSPLACEHOLDER gmail.com>
# Copyright 2019- Fabricio Cannini

from spack import *
from spack.util import *

import os

class Openmolcas(CMakePackage):
    """
    OpenMolcas is a quantum chemistry software package
    developed by scientists and intended to be used by scientists.
    It includes programs to apply many different
    electronic structure methods to chemical systems,
    but its key feature is the multiconfigurational approach,
    with methods like CASSCF and CASPT2.
    OpenMolcas is not a fork or reimplementation of Molcas,
    it is a large part of the Molcas codebase that has been released as
    free and open-source software (FOSS)
    under the Lesser General Public License (LGPL).
    Some parts of Molcas remain under a different license
    by decision of their authors (or impossibility to reach them),
    and are therefore not included in OpenMolcas.
    """

    homepage = "https://gitlab.com/Molcas/OpenMolcas"
    url      = "https://gitlab.com/Molcas/OpenMolcas/-/archive/v18.09/OpenMolcas-v18.09.tar.bz2"  # noqa

    version('18.09', sha256='255920df9e71ffdd327c84ada9e5039a2d899ac51d06162401f92a6a9452ed77')  # noqa

    variant('mpi', default=True)
    variant('openmp', default=False)
    variant('hdf5', default=False)

    depends_on('cmake@2.8.11:', type='build')
    # Minimal python 3 version according to 'Tools/pymolcas/README'
    depends_on('python@3.4:')
    depends_on('py-six')
    depends_on('py-pyparsing')
    depends_on('openblas+ilp64')
    depends_on('openblas+ilp64 threads=openmp', when='+openmp')
    depends_on('mpi', when='+mpi')
    depends_on('globalarrays', when='+mpi')
    depends_on('hdf5+mpi', when='+hdf5')

    # TODO: enable serial hdf5 support
    conflicts('~mpi', when='+hdf5')

    # TODO: find a way to put 'pymolcas'in the right directory
    def setup_environment(self, spack_env, run_env):
        """
        Due to historical reasons coming from Molcas install procedure,
        this env variable must be set so it doesn't puts 'pymolcas'
        in the first directory of 'PATH' instead of 'self.prefix.bin'
        See https://gitlab.com/Molcas/OpenMolcas/issues/2 and
        https://gitlab.com/Molcas/OpenMolcas/issues/70
        """
        spack_env.prepend_path('PATH', self.prefix.bin)

    def cmake_args(self):
        spec = self.spec

        args = []
        args.append('-DLINALG=OpenBLAS')
        args.append('-DOPENBLASROOT={0}'.format(spec['openblas'].prefix))

        if '+mpi' in self.spec:
            args.append('-DMPI=ON')
            args.append('-DCMAKE_C_COMPILER={0}'.format(
                spec['mpi'].mpicc)
            )
            args.append('-DCMAKE_Fortran_COMPILER={0}'.format(
                spec['mpi'].mpifc)
            )
            args.append('-DGA=ON')
            args.append('-DGA_INCLUDE_PATH={0}'.format(
                spec['globalarrays'].prefix.include)
            )
            args.append('-DLIBGA={0}'.format(
                spec['globalarrays'].prefix.lib.join('libga.a'))
            )
            args.append('-DLIBARMCI={0}'.format(
                spec['globalarrays'].prefix.lib.join('libarmci.a'))
            )

        if '+hdf5' in self.spec:
            args.append('-DHDF5_IS_PARALLEL=ON')
            args.append('-DHDF5_C_COMPILER_EXECUTABLE={0}'.format(
                spec['hdf5'].prefix.bin.join('h5pcc'))
            )

        if '+openmp' in self.spec:
            args.append('-DOPENMP=ON')

        return args


    #find if and where 'pymolcas' was incorrectly installed and fix it
    # Yes, it's ugly as a 3-spaces tabbed C-shell script,
    # but it'll be needed until I can find a more elegant and permanent fix
    @run_after('install')
    def post_install(self):
        for dir in os.getenv('PATH').split(os.pathsep):
            pymolcas = os.path.join(dir, 'pymolcas')
            # if I've found a file
            if os.path.isfile(pymolcas) is True:
                # And it's not at the right place
                if os.path.isfile(self.prefix.bin.join('pymolcas')) is False:
                    os.rename(pymolcas, self.prefix.bin.join('pymolcas'))
