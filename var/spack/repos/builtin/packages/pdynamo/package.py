# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
from spack.util import *

class Pdynamo(Package):
#class Pdynamo(PythonPackage):
    """
    pDynamo is an open source program library that has been designed
    for the simulation of molecular systems using quantum chemical (QC),
    molecular mechanical (MM) and hybrid QC/MM potential energy functions.
    """

    homepage = "http://www.pdynamo.org"
    url      = "http://www.pdynamo.org/pDynamo-1.9.0.tgz"

    version("1.9.0", sha256="6211deaaadebcee481499e0ea817c83bca662d298f3bc65b8ebbb05fc80f4ad0") # noqa

    variant("openmp", default=False, description="Enable OpenMP multi-threading")

    # apparently spack's atlas has no openmp support,
    # so I'll have to hardcode openblas here
    # unitl someone modify it to support mkl.
    depends_on("openblas", when="~openmp")
    depends_on("openblas threads=openmp", when="+openmp")
    depends_on("python@:2.8")
    depends_on("py-cython", type="build")
    depends_on("py-pyyaml")

    def install(self, spec, prefix):
        spec = self.spec

        blas = LibraryList(spec['blas'].libs)
        install_util = FileFilter("installation/InstallUtilities.py")
        install_util.filter("_SystemLibraryPaths\s+=.*$", "_SystemLibraryPaths = [\'/usr/lib64\'] ")
        install_util.filter("_AtlasLibraryPaths\s+=.*$", "_AtlasLibraryPaths = [\'" + spec['blas'].prefix.lib + "\']")
        install_util.filter("_AtlasSerialLibraries\s+=.*$", "_AtlasSerialLibraries = " + str(blas.names))

        install_py = FileFilter("installation/Install.py")
        install_py.filter("\"\"\"pDynamo installation script.\"\"\"", "#!/usr/bin/env python\n\"\"\"pDynamo installation script.\"\"\"")
        set_executable("installation/Install.py")
        pdyn_install = Executable("installation/Install.py")
        if '+openmp' in spec:
            pdyn_install("-f", "--openMP")
        else:
            pdyn_install("-f")
        
        pdyn_install_dir = join_path(spec["python"].prefix.lib,\
                            'python{0}',\
                            'site-packages',\
                            "pdynamo").format(
                                    spec["python"].version.up_to(2))


        install_tree('./pCore-1.9.0', pdyn_install_dir)
        install_tree('./pBabel-1.9.0', pdyn_install_dir)
        install_tree('./pMolecule-1.9.0', pdyn_install_dir)
        install_tree('./pMoleculeScripts-1.9.0', pdyn_install_dir)

    def post_install(self, spec, prefix):
        return []

