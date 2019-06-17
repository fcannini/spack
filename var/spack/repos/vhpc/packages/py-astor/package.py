# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-astor
#
# You can edit this file again by typing:
#
#     spack edit py-astor
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyAstor(PythonPackage):
    """
    AST (Abstract Syntax tree) observe/rewrite.
    astor is designed to allow easy manipulation of Python source via the AST.
    """
    homepage = "https://github.com/berkerpeksag/astor"
    url      = homepage + "/archive/0.8.tar.gz"

    version('0.8', sha256='e1161080b18ac49498e9a2fe6d4914072b06312fa4d373c980f61a907d86a00e')

    depends_on('python@3.4:')
    depends_on('py-setuptools', type='build')
    depends_on('py-wheel', type='build')

    def build_args(self, spec, prefix):
        args = []
        return args
