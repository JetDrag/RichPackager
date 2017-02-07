# coding=utf-8
import codecs

from setuptools import setup

__author__ = 'lawrentwang'

VERSION = '0.1.1'
with codecs.open('main_version', 'w', encoding='utf8') as fw:
    fw.write(VERSION)

with codecs.open("README.md", "r", encoding='utf8') as fp:
    long_description = fp.read()

setup(
    name='RichPackager',
    version=VERSION,
    description='Python package suite to ship with standard package (built by Setuptools), project data files, '
                'offline dependence and others.',
    author='Wang',
    author_email='taptube@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords='',
    py_modules=['rich_packager'],
    package_data={},
    include_package_data=True,
    zip_safe=True,
    long_description=long_description,
)
