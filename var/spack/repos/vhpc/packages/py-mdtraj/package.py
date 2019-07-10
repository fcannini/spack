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
#     spack install py-mdtraj
#
# You can edit this file again by typing:
#
#     spack edit py-mdtraj
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyMdtraj(PythonPackage):
    """
	MDTraj: A modern, open library for the analysis of molecular dynamics trajectories
	MDTraj is a python library that allows users to manipulate molecular dynamics
	(MD) trajectories and perform a variety of analyses, including fast RMSD,
	solvent accessible surface area, hydrogen bonding, etc. A highlight of MDTraj
	is the wide variety of molecular dynamics trajectory file formats which are
	supported, including RCSB pdb, GROMACS xtc, tng, and trr, CHARMM / NAMD dcd,
    AMBER binpos, AMBER NetCDF, AMBER mdcrd, TINKER arc and MDTraj HDF5.
	"""

    homepage = "https://github.com/mdtraj/mdtraj"
    url      = homepage + "/archive/1.9.3.tar.gz"

    version('1.9.3', sha256='15997a9c2bbe8a5148316a30ae420f9c345797a586369ad064b7fca9bd302bb3')

    # Mdtraj's default behavior is to enable it, so we follow
    variant('openmp', default=True, description='Enable OpenMP threading.')

    depends_on('python@:2.8,3: +tkinter', type=('build','link', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-cython', type=('build', 'link'))
    depends_on('py-numpy', type=('build','link', 'run'))
    depends_on('py-numpydoc', type='build')
    depends_on('py-scikit-learn', type=('build', 'link', 'run'))
    # Duplicated depends_on() because at less than 6 months to python 2 EOL,
    # node-js still can't bring themselves to use python 3. (py-jupyter-notebook depends on it)
    # No wonder it's hated so much.
    depends_on('py-matplotlib@:2.3', when='^python@:2.8', type=('build', 'link', 'run'))
    depends_on('py-ipython@:5', when='^python@:2.8', type='run')
    depends_on('vhpc.py-jupyter-notebook@:5.99.99', when='^python@:2.8', type='run')
    depends_on('py-jupyter-notebook@5:', when='^python@3:', type='run')
    depends_on('py-jinja2', type='run')
    depends_on('py-runipy', type='run')
    depends_on('py-pytables', type=('build', 'link', 'run'))
    # setting an option of a dependency of a dependency
    # (py-mdtraj -> py-pytables -> hdf5) is asking too much,
    # so depends_on() explicitly to avoid a needless build of mpi
    depends_on('hdf5 ~mpi', type=('build', 'link'))
    depends_on('py-pytest', type='run')
    depends_on('py-pandas', type=('build', 'link', 'run'))
    depends_on('openmm', type=('build', 'link', 'run'))

    extends('python', type=('build', 'link', 'run'))

    def build_args(self, spec, prefix):
        args = []

        if '~openmp' in spec:
            args.append('--disable-openmp')

        return args

