# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install openmm
#
# You can edit this file again by typing:
#
#     spack edit openmm
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *

class Openmm(CMakePackage):
    """
    A high performance toolkit for molecular simulation.
    Use it as a library, or as an application.
    We include extensive language bindings for Python, C, C++, and even Fortran.
    The code is open source and actively maintained on Github, licensed under MIT and LGPL.
    Part of the Omnia suite of tools for predictive biomolecular simulation.
    """

    homepage = "http://openmm.org"
    url      = "https://github.com/pandegroup/openmm/archive/7.3.1.tar.gz"

    version('7.3.1', sha256='db0c1fddc3068f689931385bc4009529261300a19effc2a9d3d47e43ab752875')

    patch('fix_python_install_location.patch', when='@7.3.1:',
            sha256='196a4337fb412ef5a7eb1216025561587dc9b16b0f84de463e576fc9e77c2426')

#    variant('python', default=False, description='Builds python bindings')
    variant('cuda', default=False, description='Builds the cuda platform')
    # TODO:
    # Enable opencl without conflicting with cuda.
    # (Cuda has its own opncl stack and it conflicts with cuda (surprise!)
#    variant('opencl', default=False, description='Builds the opencl platform')

    # These dependencies look weird, I know. See the link for an explanation:
    # http://docs.openmm.org/latest/userguide/library.html#other-required-software
    # TODO: optionally enable python bindings
    depends_on('fftw')
    depends_on('cuda', when='+cuda')
    depends_on('cmake@3.1:', type='build')
    depends_on('doxygen', type='build')
    depends_on('python@3:', type=('build', 'link','run'))
#    depends_on('python@3:', type=('build', 'link','run'), when='+python')
#    depends_on('swig@3.0.5:', type='build', when='+python')
    depends_on('swig@3.0.5:', type='build')
#    depends_on('py-numpy', type='build', when='+python')
    depends_on('py-numpy', type='build')
#    depends_on('py-setuptools', type='build', when='+python')
    depends_on('py-setuptools', type='build')

    extends('python@3:')
#    extends('python@3:')

#    conflicts('+opencl', when='+cuda')
#    conflicts('+cuda', when='+opencl')

    def setup_environment(self, spack_env, run_env):
        spec = self.spec

        _py_site_packages_dir = spec['python'].package.site_packages_dir
        _openmm_python_dir = join_path(self.prefix, _py_site_packages_dir)
        run_env.prepend_path('PYTHONPATH', _openmm_python_dir)

    install_targets = ['install','PythonInstall']

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

