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
        # "spyder",
    ],
    packages=find_packages(),
    entry_points={
        "spyder.plugins": [
            "spyder_boilerplate = spyder_boilerplate.spyder.plugin:SpyderBoilerplate"
        ],
    },
    classifiers=[
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering',
    ],
)
