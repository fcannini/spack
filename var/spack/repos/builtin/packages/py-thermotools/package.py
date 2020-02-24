# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyThermotools(PythonPackage):
    """
    A lowlevel implementation of (transition-based and histogram)
    reweighting analyis methods.
    """

    homepage = "https://github.com/markovmodel/thermotools"
    url      = homepage + "/archive/0.2.7.tar.gz"

    version('0.2.7', sha256='171c0142565ef75aedf20635605846637588de098268f2c58080dbee32c2f0b9')

    depends_on('python@3:', type=('build', 'link', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-cython@0.20:', type='build')
    depends_on('py-numpy@1.7:', type=('build', 'run'))
    depends_on('py-scipy@0.11:', type=('build', 'run'))
    depends_on('py-msmtools@1.1.3:', type=('build', 'run'))

    extends('python')
