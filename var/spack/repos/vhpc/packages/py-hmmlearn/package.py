# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyHmmlearn(PythonPackage):
    """
    hmmlearn is a set of algorithms for unsupervised learning and inference of Hidden Markov Models.
    """

    homepage = "https://github.com/hmmlearn/hmmlearn"
    
    # Pulling from pipy.org is not recommended,
    # but 'setuptools-scm' complained about using tarballs from github
    url      = "https://files.pythonhosted.org/packages/d7/c5/91b43156b193d180ed94069269bcf88d3c7c6e54514a8482050fa9995e10/hmmlearn-0.2.2.tar.gz"

    version('0.2.2', sha256='0492fe138bf6e2b95aa1efadc5124fa02ab01ba75451cd67dcc5f2a2fb282c20')

    depends_on('py-setuptools', type='build')
    depends_on('py-setuptools-scm', type='run')
    depends_on('py-cython', type='build')
    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-scipy', type=('build', 'run'))

    extends('python', type=('build', 'link', 'run'))

