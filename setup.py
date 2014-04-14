#coding:utf-8
'''

'''
import os
import sys

from setuptools import setup, find_packages


setup(
    name = "ops",
    version = "0.0.1",
    packages = find_packages(),

    include_package_data = True,

    entry_points = {
        'console_scripts' : [
            'ops_server = ops.main:start_application'
        ],
    },
    package_data = {
    },
    install_requires=[
        'tornado',
        'xlwt',
        'mysql-python',
    ],
    author = "lishengjia",
    author_email = '825137600@qq.com',
    url = "https://github.com/lishengjia",
    description = 'a system for ops',
)

