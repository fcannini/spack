# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyMsmtools(PythonPackage):
    """
    an open source collection of algorithms for the estimation and analysis
    of discrete state space Markov chains via Markov state models (MSM).
    """

    homepage = "https://github.com/markovmodel/msmtools"
    url      = homepage + "/archive/v1.2.4.tar.gz"

    version('1.2.4', sha256='64224318a723605daf1524a15724e2a4a13ed9cf43e7e37652b4c6bda7e69d44')

    depends_on('python@3:', type=('build', 'link', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-cython', type='build')
    depends_on('py-decorator', type=('build', 'run'))
    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-scipy', type=('build', 'run'))

    extends('python')
