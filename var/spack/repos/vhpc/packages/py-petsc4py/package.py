# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPetsc4py(PythonPackage):
    """This package provides Python bindings for the PETSc package.
    """

    homepage = "https://bitbucket.org/petsc/petsc4py"
    url      = "https://bitbucket.org/petsc/petsc4py/get/3.10.0.tar.gz"
    git      = "https://bitbucket.org/petsc/petsc4py.git"

    maintainers = ['dalcin', 'balay']

    version('develop', branch='master')
    version('3.11.0', sha256='50a7bbca76000da287d5b18969ddf4743b360bda1f6ee3b43b5829095569cc46')
    version('3.10.1', sha256='4eae5eaf459875b1329cae36fa1e5e185f603e8b01a4e05b59b0983c02b5a174')
    version('3.10.0', sha256='737e7812ccc54b1e0d6e8de4bdcd886c8ce287129297831f1f0e33089fa352f2')
    version('3.9.1',  sha256='9bad0bab69a19bbceb201b9203708104a0bbe0ee19c0fa839b6ea6aa55dc238c')
    version('3.9.0',  sha256='034d097b88ae874de712785f39f9d9a06329da071479c0dd834704dc6885dc97')
    version('3.8.1',  sha256='da07ffef7da61164ad75b23af59860fea467ae47532302d91b7b4ec561aa0f9c')
    version('3.8.0',  sha256='b9b728e39245213cd8e74cf4724be9bb48bd295f99634135e37dbbdbec275244')
    version('3.7.0',  sha256='fb78b50c596c3ba6a097751dd9a379e7acaf57edd36311a3afa94caa4312ee08')
    version('3.6.0',  sha256='db9d0f5bc7fa59514f7458c722f228e7d05e3dfe2858710f285faaceaf0c95cd')
    version('3.5.1',  sha256='6d942d785839bf64e1141277a728e7a0fe9ce77c98993523e9cc76691952a2fc')
    version('3.5',    sha256='20de5edd213442973a4fd043f28d55fad3653781dbe7a55795663db3934717b1')
    version('3.4',    sha256='96db5574e54804f1737f65f9f1037c7a32f0871c1ef3c77e3458d6768e0cf9d9')
    version('3.3.1',  sha256='a6ce414b9488704900c905dfb3f466c1ae14d2cfee914800e16c78a3d0ef5634')
    version('3.3',    sha256='36a669bbb113b1870fe8804193a18347390093241537acbeb7a64f3f8260ddb7')
    version('1.2',    sha256='4db7b23842ad447550f0143b888de523d2184a525fc33999d662ed22f842a8a3')
    version('1.1.2',  sha256='722956a5b78764d42c5ba78120cf46da493956aafe3d35ca7f2ff3321ddf8ad5')
    version('1.1.1',  sha256='cb65c2888863ae68eb14d62531dd07989b0de7b53806c3dd47fb416d55b37373')
    version('1.1',    sha256='03624b17047b405c73de7c34ba89565eedeb592a27a499505ad99ace1d78e083')
    version('1.0.3',  sha256='d80bf3b8ba376cd43f23e6f9ba34e8963f9bac652f0692a2e257d97759da2740')
    version('1.0.2',  sha256='26aa47ff68b0e39ffdccd5396ccdf91e267eeb83b46e72f879fc879fa4a6bdee')
    version('1.0.1',  sha256='194299e527a4c3e57506008ef03bacf90e1c4f23dcc28eac1684bd077c39dd0a')
    version('1.0',    sha256='e7135459db33999bd1b26ce7d56100747fdba28423e43d0effd18f83faee2cef')

    depends_on('py-cython', type='build', when='@develop')
    depends_on('python@2.6:2.8,3.3:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-mpi4py', type=('build', 'run'))

    depends_on('petsc+mpi')
    depends_on('petsc@develop+mpi', when='@develop')
    depends_on('petsc@3.11:3.11.99+mpi', when='@3.11:3.11.99')
    depends_on('petsc@3.10.3:3.10.99+mpi', when='@3.10.1:3.10.99')
    depends_on('petsc@3.10:3.10.2+mpi', when='@3.10.0')
    depends_on('petsc@3.9:3.9.99+mpi', when='@3.9:3.9.99')
    depends_on('petsc@3.8:3.8.99+mpi', when='@3.8:3.8.99')
    depends_on('petsc@3.7:3.7.99+mpi', when='@3.7:3.7.99')
    depends_on('petsc@3.6:3.6.99+mpi', when='@3.6:3.6.99')
