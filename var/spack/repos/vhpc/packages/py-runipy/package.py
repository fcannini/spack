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
#     spack install py-runipy
#
# You can edit this file again by typing:
#
#     spack edit py-runipy
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyRunipy(PythonPackage):
    """Run IPython notebooks from the command line"""

    homepage = "https://pypi.org/project/runipy"
    url      = "https://pypi.io/packages/r/runipy/runipy-0.1.5.tar.gz"

    version('0.1.5', sha256='389c88909fcabc330ec4e3b52b10358e978a09c4ec2e6fbf59046dee01c66839')

    patch('fix-setup-readme.patch', when='^python@3.5.0:3.5.99',
            sha256='036b948944ddc9e2533a4935c5a769c35efe28b61b1ec72ecbb3e96da1e3888e')

    depends_on('python@3:', type=('run', 'build'))
    depends_on('py-ipython@2.3.1:', type='run')
    depends_on('vhpc.py-backcall', type='run')
    depends_on('py-jinja2@2.7.2:', type='run')
    depends_on('py-pygments@1.6:', type='run')
    depends_on('py-setuptools', type='build')
    depends_on('py-vcversioner', type='build')
    depends_on('py-ipykernel@4.0.0', when='^py-ipython@4.0.0:')
    depends_on('py-nbconvert@4.0.0', when='^py-ipython@4.0.0:')
    depends_on('py-nbformat@4.0.0', when='^py-ipython@4.0.0:')

    extends('python@3:')

    def build_args(self, spec, prefix):
        args = []
        return args
