import sys

try:
    from setuptools import setup
    using_setuptools = True
except ImportError:
    from distutils.core import setup
    using_setuptools = False

from os.path import join, dirname

version = "1.2.0.2"

setup_args = {
    'name': 'scrapydArt',
    'version': version,
    'url': 'https://github.com/dequinns/scrapydart',
    'description': 'Scrapyd Plus, auth, order, filter……',
    'long_description': open('README.rst').read(),
    'author': 'quinns',
    'maintainer': 'quinns',
    'maintainer_email': 'quinns@aliyun.com',
    'license': 'BSD',
    'packages': ['scrapyd'],
    'include_package_data': True,
    'zip_safe': False,
    'classifiers': [
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: No Input/Output (Daemon)',
        'Topic :: Internet :: WWW/HTTP',
    ],
}


if using_setuptools:
    setup_args['install_requires'] = [
        'Twisted>=8.0',
        'Scrapy>=1.0',
        'six',
        'enum-compat',
    ]
    setup_args['entry_points'] = {'console_scripts': [
        'scrapydart = scrapyd.scripts.scrapyd_run:main'
    ]}
else:
    setup_args['scripts'] = ['scrapyd/scripts/scrapyd_run.py']

setup(**setup_args)
