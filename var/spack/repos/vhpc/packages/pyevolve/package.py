# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Pyevolve(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://pyevolve.sourceforge.net"
    url      = "https://github.com/perone/Pyevolve"
    git      = url + '.git'

    # FIXME: Add proper versions and checksums here.
    version('master', branch='master')

    # FIXME: Add dependencies if required.
    depends_on('py-numpy@:1.16.99')
    depends_on('py-matplotlib@:2.99.99')

    extends('python@:2.8')

