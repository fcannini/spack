# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class TaxilaLbm(MakefilePackage):
    """
    a parallel implementation of the Lattice Boltzmann Method
    for simulation of flow in porous and geometrically complex media.
    """

    homepage = "https://github.com/ecoon/Taxila-LBM"
    url      = homepage
    git      = url + '.git'

    version('7402aff', commit='7402aff')

    depends_on('automake', type='build')
    depends_on('python')
    depends_on('petsc@:3.6.4 ~superlu-dist')
    depends_on('py-petsc4py@3.6.0')
    depends_on('py-numpy@:1.16.99', when='^python@:2.8')
    depends_on('mpi', type=('build', 'link', 'run'))

    patch('geometry.patch',
          sha256='9b1bee4bcc7b477a4943a8038bb1d879e51d2588e8da7aa55c603c36b48fb8b4')
    patch('shlib.patch',
          sha256='38ed0a1130a5751a16b685f3ad19c7954e833ee237e1b30d105bb9a92a4f796a')

    parallel = False

    def setup_environment(self, spack_env, run_env):
        spack_env.set('TAXILA_DIR', self.stage.source_path)

    def build(self, spec, prefix):
        with working_dir('src/lbm/'):
            make()

        with working_dir('src/geometry/'):
            make()

    def install(self, spec, prefix):
        mkdirp(prefix.bin, prefix.lib, prefix.include)

        install('lib/lbm.a', prefix.lib)
        install('lib/liblbm.so', prefix.lib)
        install('src/geometry/createGeom2DPetsc', prefix.bin)
        install('src/geometry/createGeom3DPetsc', prefix.bin)
        install('include/lbm_definitions.h', prefix.include) 
