#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import codecs
from setuptools import setup
import {{package_name}}

AUTHOR = 'TODO'
AUTHOR_EMAIL = 'TODO'
GITHUB_ACCOUNT = 'TODO'

NAME = '{{full_project_name}}'
DESC = '{{package_name}} textX language'
VERSION = {{package_name}}.__version__
AUTHOR = __author__.split('<')[0].strip()
AUTHOR_EMAIL = __author__
LICENSE = 'MIT'
URL = 'https://github.com/%s/%s' % (GITHUB_ACCOUNT, NAME)
DOWNLOAD_URL = 'https://github.com/%s/%s/archive/v%s.tar.gz' % \
    (GITHUB_ACCOUNT, NAME, VERSION)
README = codecs.open(os.path.join(os.path.dirname(__file__), 'README.md'),
                     'r', encoding='utf-8').read()

if sys.argv[-1].startswith('publish'):
    if os.system("pip list | grep wheel"):
        print("wheel not installed.\nUse `pip install wheel`.\nExiting.")
        sys.exit()
    if os.system("pip list | grep twine"):
        print("twine not installed.\nUse `pip install twine`.\nExiting.")
        sys.exit()
    os.system("python setup.py sdist bdist_wheel")
    if sys.argv[-1] == 'publishtest':
        os.system("twine upload -r test dist/*")
    else:
        os.system("twine upload dist/*")
        print("You probably want to also tag the version now:")
        print("  git tag -a {0} -m 'version {0}'".format(VERSION))
        print("  git push --tags")
    sys.exit()

setup(
    name = NAME,
    version = VERSION,
    description = DESC,
    long_description = README,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    maintainer = AUTHOR,
    maintainer_email = AUTHOR_EMAIL,
    license = LICENSE,
    url = URL,
    download_url = DOWNLOAD_URL,
    packages = ["{{package_name}}"],
    include_package_data=True,
    install_requires = ["textX"],
    keywords = "tools language DSL",
    entry_points={
        'textx_lang': [
            '{{package_name}} = {{package_name}}.lang:main',
        ]
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        ]

)
