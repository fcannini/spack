# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class TaxilaLbm(Package):
    """
    a parallel implementation of the Lattice Boltzmann Method
    for simulation of flow in porous and geometrically complex media.
    """

    homepage = "https://github.com/ecoon/Taxila-LBM"
    url      = homepage
    git      = url + '.git'

    version('master', branch='master')

    depends_on('petsc@:3.6.4 +debug ~superlu-dist')
    depends_on('py-petsc4py@3.7.0')
    def install(self, spec, prefix):
        make()
        make('install')
