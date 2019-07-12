# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyFastcluster(PythonPackage):
    """
    Fast hierarchical clustering routines for Python.

    This library provides Python functions for hierarchical clustering.
    It generates hierarchical clusters from distance matrices or from vector data.

    Note that this package provides **only the Python interface** for fastcluster.
    If you want to also use R, you should install the 'r-fastcluster' package instead.
    """

    homepage = "https://github.com/dmuellner/fastcluster"
    url      = homepage + "/archive/v1.1.25-2.tar.gz"

    version('1.1.25-2', sha256='40b96569f3a2b257fd41a906a77e6d6dc41302540bf53acbd0c7530fa93cad89')

    depends_on('py-setuptools', type='build')
    depends_on('py-numpy', type=('build', 'run'))
    

    def build_args(self, spec, prefix):
        args = []
        return args
