from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.3.7'
DESCRIPTION = 'A basic python script to make slowed + reverbs.'

# Setting up
setup(
    name="slowedreverb",
    version=VERSION,
    author="JustCow",
    author_email="<justcow@pm.me>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['pedalboard', 'soundfile', 'argparse'],
    keywords=['python', 'music', 'slowed reverb', 'justcow'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)