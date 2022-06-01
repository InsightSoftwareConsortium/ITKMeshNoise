# -*- coding: utf-8 -*-
from __future__ import print_function
from os import sys

try:
    from skbuild import setup
except ImportError:
    print('scikit-build is required to build from source.', file=sys.stderr)
    print('Please run:', file=sys.stderr)
    print('', file=sys.stderr)
    print('  python -m pip install scikit-build')
    sys.exit(1)

setup(
    name='itk-meshnoise',
    version='0.1.0',
    author='Davis Vigneault',
    author_email='davis.vigneault@gmail.com',
    packages=['itk'],
    package_dir={'itk': 'itk'},
    download_url=r'https://github.com/InsightSoftwareConsortium/ITKMeshNoise',
    description=r'Classes to perturb mesh objects with Gaussian noise',
    long_description='itk-meshnoise provides classes to perturb mesh objects '
                     'with Gaussian noise.\n'
                     'Please refer to:\n'
                     'Vigneault D., '
                     '"Perturbing Mesh Vertices with Additive Gaussian Noise", '
                     'Insight Journal, January-December 2016, https://hdl.handle.net/10380/3567.',
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: C++",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries",
        "Operating System :: Android",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS"
        ],
    license='Apache',
    keywords='ITK InsightToolkit Mesh Noise',
    url=r'https://github.com/InsightSoftwareConsortium/ITKMeshNoise',
    install_requires=[
        r'itk>=5.1.1'
    ]
    )
