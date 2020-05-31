# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2020, Gonzalo Peña-Castellanos
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------
"""
Spyder Boilerplate setup.
"""

# Third party imports
from setuptools import find_packages, setup

# Local imports
from spyder_boilerplate import __version__


setup(
    # See: https://setuptools.readthedocs.io/en/latest/setuptools.html
    name="spyder-boilerplate",
    version=__version__,
    author="Gonzalo Peña-Castellanos",
    author_email="goanpeca@example.com",
    description="Boilerplate needed to create a Spyder Plugin.",
    license="MIT license",
    url="https://github.com/goanpeca/spyder-boilerplate",
    install_requires=[
        "qtpy",
        "qtawesome",
    ],
    packages=find_packages(),
    entry_points={
        "spyder.plugins": [
            "spyder_boilerplate = spyder_boilerplate.spyder.plugin:SpyderBoilerplate"
        ],
    }
)
