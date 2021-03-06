#    Copyright 2013 - 2016 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os

from setuptools import find_packages
from setuptools import setup


setup(
    name='fuel-devops',
    version='3.0.0',
    description='Library for creating and manipulating virtual environments',
    author='Mirantis, Inc.',
    author_email='product@mirantis.com',
    url='http://mirantis.com',
    keywords='devops virtual environment',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
    data_files=[
        (os.path.expanduser('~/.devops'), ['devops/log.yaml']),
        (os.path.expanduser('~/.devops/log'), [])],
    scripts=['bin/dos.py'],
    install_requires=[
        'netaddr>=0.7.12,!=0.7.16',
        'paramiko>=1.16.0',
        'Django>=1.8,<1.9',
        'jsonfield',
        'psycopg2>=2.5',
        'PyYAML>=3.1.0',
        'libvirt-python',
        'tabulate',
        'six>=1.9.0',
    ],
    tests_require=[
        'pytest>=2.7.1',
        'pytest-django >= 2.8.0',
        'mock>=1.2',
        'tox'
    ],
)
