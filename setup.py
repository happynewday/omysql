#!/usr/bin/env python
#coding=utf8

try:
    from  setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
        name = 'omysql',
        version = '1.0',
        install_requires = [], 
        description = 'provide mysql api',
        url = 'https://github.com/zhouxianggen//pymysql', 
        author = 'zhouxianggen',
        author_email = 'zhouxianggen@gmail.com',
        classifiers = [ 'Programming Language :: Python :: 3.7',],
        packages = ['omysql'],
        data_files = [ ],  
        entry_points = { }   
        )
