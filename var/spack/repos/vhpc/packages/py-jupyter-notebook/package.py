# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyJupyterNotebook(PythonPackage):
    """Jupyter Interactive Notebook"""

    homepage = "https://github.com/jupyter/notebook"
    url      = "https://github.com/jupyter/notebook/archive/4.2.3.tar.gz"

    version('5.7.8', sha256='b4691f40924eca3c9dabf0bf6b1884aef76aa7e380f4c37781cf18b3a2f72702')
    version('5.7.7', sha256='ce7791cf411fd51e3259689874076250956c9cf2594fae230d4066b7d29ff1c4')
    version('5.7.6', sha256='3b44cdb06d9f954fc3790dd0641fef0ff1ec5c54a46ac3ba110b9d36d3570057')
    version('5.7.5', sha256='81f6e377ee2ee58862755472a12935438830fd9878b89a61dba7baede7ae3751')
    version('5.7.4', sha256='c26c67ee16a64b6d2444884b73c399d8020f598f833f4165864e31f28d1c410e')
    version('5.7.3', sha256='db4d64ef1e246127808aaba58614d437326e3d02ea7f37011bbd488db403046c')
    version('5.7.2', sha256='b54a678be4eaa60231ceb1e0eb8779f91018825c4543dcb1cca8573ba9d72708')
    version('5.7.1', sha256='60d468e0e0dc0476f532b75eec69bcf774a9e47afb6bb827b045448ebe4b18c8')
    version('5.7.0', sha256='99b58a62d5c0172b642341e21ab19a7e171f462d632c45b97286a56f59af6b6b')
    version('5.6.0', sha256='3d5b738bea8eaef944fffe261746b063e9ca5e89257b76d5f623cce816df4864')
    version('4.2.3', '5c6b0b1303adacd8972c4db21eda3e98')
    version('4.2.2', '7f9717ae4fed930d187a44c0707b6379')
    version('4.2.1', '4286f1eaf608257bd69cad4042c7c2fe')
    version('4.2.0', '136be6b72fe9db7f0269dc7fa5652a62')
    version('4.1.0', '763ab54b3fc69f6225b9659b6994e756')
    version('4.0.6', 'd70d8a6d01893f4b64df9edbc0e13b52')
    version('4.0.5', '2681a70e4c62aafe7ce69f1da5799ac8')
    version('4.0.4', 'ab72f28f6af8107d71241a4110e92c05')
    version('4.0.3', '119beea793865ee4b1673a50043ead2a')
    version('4.0.2', '77f371e9a23a840d14d8a60fee7ba1b7')

    variant('terminal', default=False, description="Enable terminal functionality")

    depends_on('python@2.7:2.8,3.3:')
    depends_on('npm', type='build')
    depends_on('node-js', type=('build', 'run'))
    depends_on('py-jinja2', type=('build', 'run'))
    depends_on('py-tornado@4:', type=('build', 'run'))
    depends_on('py-ipython-genutils', type=('build', 'run'))
    depends_on('py-traitlets', type=('build', 'run'))
    depends_on('py-jupyter-core', type=('build', 'run'))
    depends_on('py-jupyter-client', type=('build', 'run'))
    depends_on('py-jupyter-console', type=('build', 'run'))
    depends_on('py-nbformat', type=('build', 'run'))
    depends_on('py-nbconvert', type=('build', 'run'))
    depends_on('py-ipykernel@5.1.0:', when='@4.2.0: ^python@3.4:', type=('build', 'run'))
    depends_on('py-ipykernel@:4.99.99', when='^python@:2.8', type=('build', 'run'))
#    depends_on('py-ipykernel@5:', when='^python@3.4:', type=('build', 'run'))
    depends_on('py-terminado@0.3.3:', when="+terminal", type=('build', 'run'))
    depends_on('py-ipywidgets', when="+terminal", type=('build', 'run'))
