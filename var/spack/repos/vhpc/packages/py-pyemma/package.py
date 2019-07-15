# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPyemma(PythonPackage):
    """
    EMMA = Emma's Markov Model Algorithms) is an open source Python/C package
    for analysis of extensive molecular dynamics simulations.
    """

    homepage = "http://www.pyemma.org"
    url      = "https://github.com/markovmodel/PyEMMA"
    git      = "https://github.com/markovmodel/PyEMMA.git"

    versions = ['2.5.4']

    for v in versions:
        version('{0}'.format(v), tag='v{0}'.format(v), submodules=True)

    depends_on('cmake', type='build')
    depends_on('python@:2.8,3:', type=('build', 'link', 'run'))
#    depends_on('python@3:', when='@2.5.5:', type=('build', 'link', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-bhmm@0.6:0.6.99')
    depends_on('py-decorator@4:')
    depends_on('py-h5py@2.7.1: ~mpi')
    depends_on('py-matplotlib@:2.2.99', when='^python@:2.8')
    depends_on('py-matplotlib@3:', when='^python@3:')
    depends_on('py-numpy@1.8.0:')
    depends_on('py-pathos')
    depends_on('py-psutil@3.1.1:')
    depends_on('py-pyyaml')
    depends_on('py-scipy@0.11:')
    depends_on('py-cython')
    depends_on('py-tqdm')
    depends_on('py-mdtraj')
    depends_on('hdf5 ~mpi', type='build')

    extends('python')
