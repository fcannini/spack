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
#     spack install py-msmbuilder
#
# You can edit this file again by typing:
#
#     spack edit py-msmbuilder
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyMsmbuilder(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://github.com/msmbuilder/msmbuilder"
    url      = homepage + "/archive/3.8.0.tar.gz"

    version('3.8.0', sha256='dc9b8500887cbd64dff3a921c884d31a8d3f17fd29063d26a83153535434c1c0')

    # https://github.com/msmbuilder/msmbuilder/pull/1102
    patch('https://github.com/msmbuilder/msmbuilder/commit/9a9d40fe4b0d1de2b508634cdb0f166d75e93d0d.patch',
        sha256='9e18e08363cdce31de07a2cf81adc6fd9e0a6634a8d181d42255d8139920d818')

    # Fixes running tests 
    patch('sklearn.grid_search.patch',
            sha256='3c1c31be4f939c72e736d0e472aa1c62542cd59c4a0733d4a399037da7209b14')

    # Msmbuilder default behavior is to enable it, so we follow
    variant('openmp', default=True, description='Enable OpenMP threading.')

    depends_on('python@:2.8,3.4:', type=('build', 'link', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-six', type=('build', 'run'))
    depends_on('py-cython@0.18:', type=('build', 'link'))
    depends_on('py-numpy', type=('build', 'link', 'run'))
    depends_on('py-numpydoc', type='build')
    depends_on('py-scikit-learn', type=('build', 'link', 'run'))
    depends_on('py-pytables', type=('build', 'link', 'run'))
    # setting an option of a dependency of a dependency
    # (py-msmbuilder -> py-pytables -> hdf5) is asking too much,
    # so depends_on() explicitly to avoid a needless build of mpi
    depends_on('hdf5 ~mpi', type=('build', 'link'))
    depends_on('py-pandas', type=('build', 'link', 'run'))
    depends_on('py-mdtraj@1.1:', type=('build', 'link', 'run'))
   

    extends('python', type=('build', 'link', 'run'))

    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args

        if '~openmp' in spec:
            args.append('--disable-openmp')

        return args

