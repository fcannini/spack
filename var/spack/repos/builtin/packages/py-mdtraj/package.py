# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyMdtraj(PythonPackage):
    """
    MDTraj: A modern, open library for the analysis
    of molecular dynamics trajectories
    """

    homepage = "https://github.com/mdtraj/mdtraj"
    url      = homepage + "/archive/1.9.3.tar.gz"

    version('1.9.3', sha256='15997a9c2bbe8a5148316a30ae420f9c345797a586369ad064b7fca9bd302bb3')

    # Mdtraj's default behavior is to enable it, so we follow
    variant('openmp', default=True, description='Enable OpenMP threading.')

    depends_on('openmm', type=('build', 'link', 'run'))
    depends_on('python@3: +tkinter', type=('build', 'link', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-numpydoc', type='build')
    depends_on('py-cython', type='build')
    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-scikit-learn', type=('build', 'run'))
    depends_on('py-matplotlib@3:', type=('build', 'run'))
    depends_on('py-jupyter-notebook@5:', type='run')
    depends_on('py-tables', type=('build', 'run'))
    depends_on('py-pandas', type=('build', 'run'))
    depends_on('py-ipython@5:', type='run')
    depends_on('py-pytest', type='run')
    depends_on('py-jinja2', type='run')
    depends_on('py-runipy', type='run')

    extends('python')

    def build_args(self, spec, prefix):
        args = []

        if '~openmp' in spec:
            args.append('--disable-openmp')

        return args
