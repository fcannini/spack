# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import platform
import sys
import os
from spack import *


class Namd(MakefilePackage):
    """NAMDis a parallel molecular dynamics code designed for
    high-performance simulation of large biomolecular systems."""

    homepage = "http://www.ks.uiuc.edu/Research/namd/"
    url      = "file://{0}/NAMD_2.12_Source.tar.gz".format(os.getcwd())

    version('2.9', sha256='9ba6a1f87d4600a62847728d7c223295be214f9a72b5bb62552f74d644108424')
    version('2.10', sha256='a5282c172524c2fbe6b9ba56f2de8c84f1093405c914ffbc70442dd0dd4e4289')
    version('2.11', sha256='4de1a8c95d7ad3dc3b4ce22f261cec85beb8d06b332d016c28e432d9986f0789')
    version('2.12', '2a1191909b1ab03bf0205971ad4d8ee9')
    version('2.13', sha256='cb0b43f520ac6be761899326441541aa00de15897986223c8ce2f0f6e42b52bc')

    variant('fftw', default='3', values=('none', '2', '3', 'mkl'),
            description='Enable the use of FFTW/FFTW3/MKL FFT')

    variant('interface', default='none', values=('none', 'tcl', 'python'),
            description='Enables TCL and/or python interface')

    depends_on('charmpp')

    depends_on('fftw@:2.99', when="fftw=2")
    depends_on('fftw@3:', when="fftw=3")

    depends_on('intel-mkl', when="fftw=mkl")

    depends_on('tcl', when='interface=tcl')

    depends_on('tcl', when='interface=python')
    depends_on('python', when='interface=python')

    def _copy_arch_file(self, lib):
        config_filename = 'arch/{0}.{1}'.format(self.arch, lib)
        copy('arch/Linux-x86_64.{0}'.format(lib),
             config_filename)
        if lib == 'tcl':
            filter_file(r'-ltcl8\.5',
                        '-ltcl{0}'.format(self.spec['tcl'].version.up_to(2)),
                        config_filename)

    def _append_option(self, opts, lib):
        if lib != 'python':
            self._copy_arch_file(lib)
        spec = self.spec
        opts.extend([
            '--with-{0}'.format(lib),
            '--{0}-prefix'.format(lib), spec[lib].prefix
        ])

    @property
    def arch(self):
        plat = sys.platform
        if plat.startswith("linux"):
            plat = "linux"
        march = platform.machine()
        return '{0}-{1}'.format(plat, march)

    @property
    def build_directory(self):
        return '{0}-spack'.format(self.arch)

    def edit(self, spec, prefix):
        with working_dir('arch'):
            with open('{0}.arch'.format(self.build_directory), 'w') as fh:
                # this options are take from the default provided
                # configuration files
                optims_opts = {
                    'gcc': '-m64 -O3 -fexpensive-optimizations -ffast-math',
                    'intel': '-O2 -ip'
                }

                optim_opts = optims_opts[self.compiler.name] \
                    if self.compiler.name in optims_opts else ''

                fh.write('\n'.join([
                    'NAMD_ARCH = {0}'.format(self.arch),
                    'CHARMARCH = ',
                    'CXX = {0.cxx} {0.cxx11_flag}'.format(
                        self.compiler),
                    'CXXOPTS = {0}'.format(optim_opts),
                    'CC = {0}'.format(self.compiler.cc),
                    'COPTS = {0}'.format(optim_opts),
                    ''
                ]))

        self._copy_arch_file('base')

        opts = ['--charm-base', spec['charmpp'].prefix]
        fftw_version = spec.variants['fftw'].value
        if fftw_version == 'none':
            opts.append('--without-fftw')
        elif fftw_version == 'mkl':
            self._append_option(opts, 'mkl')
        else:
            _fftw = 'fftw{0}'.format('' if fftw_version == '2' else '3')

            self._copy_arch_file(_fftw)
            opts.extend(['--with-{0}'.format(_fftw),
                         '--fftw-prefix', spec['fftw'].prefix])

        interface_type = spec.variants['interface'].value
        if interface_type != 'none':
            self._append_option(opts, 'tcl')

            if interface_type == 'python':
                self._append_option(opts, 'python')
        else:
            opts.extend([
                '--without-tcl',
                '--without-python'
            ])

        config = Executable('./config')

        config(self.build_directory, *opts)

    def install(self, spec, prefix):
        with working_dir(self.build_directory):
            mkdirp(prefix.bin)
            install('namd2', prefix.bin)

            # I'm not sure this is a good idea or if an autoload of the charm
            # module would not be better.
            install('charmrun', prefix.bin)
