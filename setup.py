from distutils.core import setup
from setuptools import find_packages
import os
import sys
from subprocess import Popen,PIPE

#README = open('README.rst').read()

def all_files(path,num_root_dir_to_skip=1):
    all= map(lambda x: x.strip(),Popen(['find',path],stdout=PIPE).stdout.readlines())
    return map(lambda x: '/'.join(x.split('/')[num_root_dir_to_skip:]), filter(os.path.isfile,all))

setup(name='Erik',
    version='0.0.5',
    description = "Erik Misc",
    author='Erik Gafni',
    license='Non-commercial',
    long_description='Misc scripts',
    packages=find_packages(),
    install_requires=[
    ]
)