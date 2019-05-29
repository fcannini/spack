# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os


class Amber(CMakePackage):
    """Amber is a suite of biomolecular simulation programs."""

    homepage = 'http://ambermd.org'
    url      = 'file://{0}/linux-AmberTools18.tar.bz2'.format(os.getcwd())

    version('18', sha256='c630fc3d251fcefe19bb81c8c617e0547f1687b6aef68ea526e4e5fff65bea1c')

    resource(name='amber-source',
            sha256='2060897c0b11576082d523fb63a51ba701bc7519ff7be3d299d5ec56e8e6e277',
            url='file://{0}/linux-Amber18.tar.bz2'.format(os.getcwd())
    )

    # url for amber update patches. As of may/2019 there 14 patches released:
    # 'http://ambermd.org/bugfixes/{0}.0/update.{1]'.format(
    # self.version, amber_patch_number)
    #
    # url for tools update patches. Same number of patches as amber so far
    # 'http://ambermd.org/bugfixes/AmberTools/{0}.0/update.{1}'.format(
    # self.version, tools_patch_number)
    patch('gpu_utils.patch', when='+cuda')
    patch('add_cuda_9.2.patch', when='+cuda')

    variant('mpi',  default=True,
            description='Uses MPI parallelism. Enabled by default')
    variant('cuda', default=False,
            description='Enable building for Nvidia GPUs')
    variant('openmp', default=False,
            description='Enable using OpenMP threading')
    variant('tools', default=True,
            description='Builds AmberTools also. Enabled by default.'
                        'Disabling speeds up installation'
                        'if you only need the main programs.')

    depends_on('cmake', type='build')
    depends_on('flex', type='build')
    depends_on('m4', type='build')
    depends_on('automake', type='build')
    depends_on('autoconf', type='build')
    depends_on('bzip2')
    depends_on('readline')
    depends_on('ncurses')
    depends_on('perl')
    depends_on('python@3.4.0:3.6.99 +tkinter')
    depends_on('py-setuptools')
    depends_on('py-numpy')
    depends_on('py-scipy')
    depends_on('py-matplotlib')
    depends_on('py-cython')
    depends_on('py-mpi4py')
    depends_on('blas')
    depends_on('lapack')
    depends_on('mpi')
    depends_on('fftw')
    depends_on('arpack-ng')
    # TODO:
    # use external builds of netcdf, netcdf-fortran and parallel-netcdf
    # depends_on('hdf5 +fortran +hl')
    # depends_on('netcdf')
    # depends_on('netcdf-fortran')
    # depends_on('parallel-netcdf')
    depends_on('boost')
    depends_on('cuda@7.5.18:9.2.999', when='+cuda')

    # http://ambermd.org/Installation.php
    conflicts('^openmpi@4:',
                msg='Caution: As of February, 2019,'
                    'Amber won\'t compile with version 4 of openmpi.'
                    'This release removes support from some'
                    'older MPI calls that we still use.'
                    'We are working on the problem.')

    # You might want to get a cup of your favorite beverage,
    # this will take a while.
    parallel = False

    def setup_dependent_environment(self, spack_env, run_env, dependent_spec):
        # This one is needed to build amber
        spack_env.set('AMBERHOME', self.stage.source_path)

        # These are needed later in the module file to run amber
        run_env.set('AMBERHOME', self.prefix)

        run_env.prepend_path('PERL5LIB', self.prefix.lib.join('perl'))

        run_env.prepend_path('PYTHONPATH', join_path(
            self.prefix.lib, join('python', spec['python'].version.up_to(2)))
        )

    def cmake_args(self):
        spec = self.spec

        _build_dir = self.stage.source_path
        _nameversion = '{0}{1}'.format(self.name, self.version)
        _amber_dir = join_path(_build_dir, _nameversion)
        _src_dirs = ['src', 'test', 'benchmarks']

        for _d in _src_dirs:
            _from_here = join_path(_amber_dir, _d)
            _to_here = join_path(_build_dir, _d)
            mkdirp(_to_here)
            copy_tree(_from_here, _to_here)

        # You can in theory run this through cmake. But after updating
        # cmake is run again and then it may be or not under spack control.
        # There be dragons.
        update_amber = Executable('./update_amber')
        update_amber('--update')

        args = []

        # This list comes from 'cmake/3rdPartyTools.cmake'
        # and will probably grow as time passes
        external_libs = ['blas', 'lapack', 'fftw', 'readline', 'mpi4py',
                         'zlib', 'libbz2', 'libm', 'boost', 'arpack']

        # This list comes from 'cmake/WhichTools.cmake'
        # and will change as new code is added to amber
        # Do not change the order of elements
        tools = ['gbnsr6', 'cifparse', 'addles', 'sander', 'nmr_aux',
                 'nmode', 'antechamber', 'sqm', 'reduce', 'sebomd',
                 'ndiff-2.00', 'cpptraj', 'pbsa', 'sff', 'rism', 'nab', 'etc',
                 'mdgx', 'xtalutil', 'saxs', 'mm_pbsa', 'paramfit', 'FEW',
                 'amberlite', 'cphstats', 'quick', 'nfe-umbrella-slice',
                 'leap', 'parmed', 'mmpbsa_py', 'pymsmt', 'pysander',
                 'pytraj', 'pymdgx', 'pdb4amber', 'packmol_memgen']

        args.append('-DCOMPILER=MANUAL')
        args.append('-DDOWNLOAD_MINICONDA=OFF')
        args.append('-DINSTALL_TESTS=OFF')
        args.append('-DBUILD_GUI=OFF')
        args.append('-DCHECK_UPDATES=OFF')
        args.append('-DAPPLY_UPDATES=OFF')
        args.append('-DBLA_VENDOR=All')

        if '~tools' in spec:
            args.append('-DDISABLE_TOOLS={0}'.format(
                ';'.join(tools))
            )

        args.append('-DFORCE_EXTERNAL_LIBS={0}'.format(
            ';'.join(external_libs))
        )

        args.append('-DCUDA={0}'.format(
            'ON' if '+cuda' in spec else 'OFF')
        )

        args.append('-DOPENMP={0}'.format(
            'ON' if '+openmp' in spec else 'OFF')
        )

        args.append('-DMPI={0}'.format(
            'OFF' if '~mpi' in spec else 'ON')
        )

        args.append('-DUSE_FFT=ON')
        args.append('-DFFTW_LIBRARIES_SERIAL={0}'.format(
            spec['fftw'].prefix.lib.join('libfftw3.so'))
        )

        # This 'if' is not needed in 99.99999999% of the times,
        # but just in case ...
        if '+mpi' in spec:
            args.append('-DFFTW_LIBRARIES_MPI={0}'.format(
                spec['fftw'].prefix.lib.join('libfftw3_mpi.so'))
            )

        # TODO:
        # use external builds of netcdf, netcdf-fortran and parallel-netcdf
        # args.append('-DNetCDF_LIBRARIES={0}'.format(
        #     spec['netcdf'].prefix.lib.join('libnetcdf.so'))
        # )

        # args.append('-DNetCDF_INCLUDES={0}'.format(
        #     spec['netcdf'].prefix.include)
        # )

        # args.append('-DNetCDF_LIBRARIES_F90={0}'.format(
        #     spec['netcdf-fortran'].prefix.lib.join('libnetcdff.so'))
        # )

        # args.append('-DPnetCDF_C_LIBRARY={0}'.format(
        #     spec['parallel-netcdf'].prefix.lib.join('libpnetcdf.so'))
        # )

        # args.append('-DPnetCDF_C_INCLUDE_DIR={0}'.format(
        #     spec['parallel-netcdf'].prefix.include)
        # )

        # args.append('-DPnetCDF_Fortran_LIBRARY={0}'.format(
        #     spec['parallel-netcdf'].prefix.lib.join('libpnetcdf.so'))
        # )

        # args.append('-DPnetCDF_Fortran_INCLUDE_DIR={0}'.format(
        #     spec['parallel-netcdf'].prefix.include)
        # )

        return args
