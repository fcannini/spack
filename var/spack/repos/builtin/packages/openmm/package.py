# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Openmm(CMakePackage):
    """
    A high performance toolkit for molecular simulation.
    Use it as a library, or as an application.
    We include extensive language bindings for Python,
    C, C++, and even Fortran.
    The code is open source and actively maintained on Github,
    licensed under MIT and LGPL.
    Part of the Omnia suite of tools for predictive biomolecular simulation.
    """

    homepage = "http://openmm.org"
    url      = "https://github.com/pandegroup/openmm/archive/7.3.1.tar.gz"

    version('7.3.1', sha256='db0c1fddc3068f689931385bc4009529261300a19effc2a9d3d47e43ab752875')

    patch('fix_python_install_location.patch', when='@7.3.1:',
          sha256='a3ab285ad946170c9323203df84544028357a5720191df1abcfc967faea43990')

    variant('cuda', default=False, description='Builds the cuda platform')

    depends_on('cmake@3.1:', type='build')
    depends_on('doxygen', type='build')
    depends_on('py-setuptools', type='build')
    depends_on('swig@3.0.5:', type='build')
    depends_on('fftw precision=float')
    depends_on('python@3:', type=('build', 'link', 'run'))
    depends_on('py-numpy', type=('build', 'run'))
    depends_on('cuda', when='+cuda')

    extends('python')

    def setup_environment(self, spack_env, run_env):
        spec = self.spec

        _py_site_packages_dir = spec['python'].package.site_packages_dir
        _openmm_python_dir = join_path(self.prefix, _py_site_packages_dir)
        run_env.prepend_path('PYTHONPATH', _openmm_python_dir)

    install_targets = ['install', 'PythonInstall']

    def cmake_args(self):
        spec = self.spec

        args = []

        # Common options
        args.append('-DOPENMM_BUILD_CPU_LIB=ON')
        args.append('-DOPENMM_BUILD_C_AND_FORTRAN_WRAPPERS=ON')
        args.append('-DCMAKE_VERBOSE_MAKEFILE=ON')
        # For whatever reason this is on by default.
        # We only want to enable it explicitly
        args.append('-DOPENMM_BUILD_OPENCL_LIB=OFF')
        args.append('-DOPENMM_BUILD_CUDA_LIB=OFF')

        # Not really needed. Perhaps add a variant if asked.
        args.append('-DOPENMM_BUILD_EXAMPLES=OFF')

        args.append('-DOPENMM_BUILD_PYTHON_WRAPPERS=ON')

        args.append('-DFFTW_INCLUDES={0}'.format(
            spec['fftw'].prefix.include)
        )

        args.append('-DFFTW_LIBRARY={0}'.format(
            spec['fftw'].prefix.lib.join('libfftw3f.so'))
        )

        args.append('-DFFTW_THREADS_LIBRARY={0}'.format(
            spec['fftw'].prefix.lib.join('libfftw3f_threads.so'))
        )

        args.append('-DOPENMM_BUILD_CUDA_LIB={0}'.format(
            'ON' if '+cuda' in spec else 'OFF')
        )

        return args
