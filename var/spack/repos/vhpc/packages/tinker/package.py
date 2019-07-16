# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from llnl.util import *
import os

class Tinker(Package):
    """
    The Tinker molecular modeling software is a complete and general package
    for molecular mechanics and dynamics, with some special features for biopolymers.
    """

    homepage = "https://dasher.wustl.edu/tinker"
    url      = homepage + "/downloads/tinker-8.7.1.tar.gz"

    version('8.7.1', sha256='0d6eff8bbc9be0b37d62b6fd3da35bb5499958eafe67aa9c014c4648c8b46d0f')

    depends_on('fftw')


    def install(self, spec, prefix):

        # each one is the basename of the scripts to build tinker,
        # cf. page 9 of the manual: https://dasher.wustl.edu/tinker/downloads/guide.pdf
        phases = ['compile',
                  'library',
                  'link',
                  'rename']

        # directories where there are binaries and/or scripts
        exec_dirs = ['bin', 'perl']

        build = self.stage.source_path
        fc = os.path.split(self.compiler.fc)[1]

        for phase in phases:
            filename = phase + '.make'
            copy(join_path(build, 'linux', fc, filename), 'source/')

        fftw_ld_flags = ' '.join(['-L' + str(spec['fftw'].libs), '-lfftw3_threads', '-lfftw3'])

        with working_dir('source/'):

            # Your cpu may or may not have it, e.g. arm or power
            arch = spec.architecture
            if arch.target != 'x86_64':
               filter_file('-mavx ', '', 'compile.make')

            filter_file('-static-libgcc ', '', 'link.make')
            filter_file('libfftw3_threads.a libfftw3.a', fftw_ld_flags, 'link.make')

            sh = which('bash')

            [sh('-v', './' + phase + '.make') for phase in phases]

        # rename to avoid overwriting a binary with the same name when installing
        with working_dir('perl/'): os.rename('bar', 'bar' + '.pl')

        # No need of this file to be in spec.prefix.bin
        with working_dir('bin/'): os.remove('0README')

        def doinstall(d):
            with working_dir(d):
                [install(f, spec.prefix.bin) for f in os.listdir('.')]

        mkdirp(spec.prefix.bin)
           
        [doinstall(dir) for dir in exec_dirs]

