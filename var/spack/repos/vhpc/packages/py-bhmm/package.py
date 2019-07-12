# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyBhmm(PythonPackage):
    """
    This toolkit provides machinery for sampling from the Bayesian posterior
    of hidden Markov models with various choices of prior and output models.
    """

    homepage = "https://github.com/bhmm/bhmm"
    url      = homepage + "/archive/0.6.3.tar.gz"

    version('0.6.3', sha256='5f16596716692144b8ac39b2d74bbed948ac601f69df152dd8763e9e8fa14024')

    depends_on('py-setuptools', type='build')
    depends_on('py-six', type='build')
    depends_on('py-cython', type='build')
    depends_on('py-numpy', type=('build', 'link', 'run'))
    depends_on('py-scipy', type=('build', 'link', 'run'))
    depends_on('py-msmtools', type=('build', 'run'))


    def build_args(self, spec, prefix):
        args = []
        return args
