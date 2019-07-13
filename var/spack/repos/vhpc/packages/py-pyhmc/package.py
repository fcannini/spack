# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPyhmc(PythonPackage):
    """
    pyhmc: Hamiltonain Monte Carlo in Python
    
    This package is a straight-forward port of the functions 'hmc2.m' and 'hmc2_opt.m'
    from the 'MCMCstuff' matlab toolbox 'http://www.lce.hut.fi/research/mm/mcmcstuff/'
    written by Aki Vehtari.
    """

    homepage = "https://pythonhosted.org/pyhmc"
    url      = "https://github.com/rmcgibbo/pyhmc/archive/0.1.2.tar.gz"

    version('0.1.2', sha256='ba3cf17c7e2e4fc4428b73d9b8fe981fe85a3f5aa36d0b079568055c7bacc607')

    depends_on('py-setuptools', type='build')
    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-cython', type=('build', 'run'))

    extends('python', type=('build', 'link', 'run'))

