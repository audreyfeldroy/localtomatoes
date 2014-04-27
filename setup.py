import re
from setuptools import setup

init_py = open('localtomatoes/__init__.py').read()
metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", init_py))
metadata['doc'] = re.findall('"""(.+)"""', init_py)[0]

setup(
    name='localtomatoes',
    version=metadata['version'],
    description=metadata['doc'],
    author=metadata['author'],
    author_email=metadata['email'],
    url=metadata['url'],
    packages=['localtomatoes'],
    include_package_data=True,
    install_requires=[
        'docopt < 1.0.0'
    ],
    entry_points={
        'console_scripts': [
            'localtomatoes = localtomatoes.cli:main',
        ],
    },
    test_suite='nose.collector',
    license=open('LICENSE').read(),
)
