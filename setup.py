from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='shrincols',
    version='0.1.0',
    description='Tool for fit string to a fixed number of cols.',
    long_description=readme,
    author='Thiago Melo',
    author_email='thiago.lc.melo@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[],
    entry_points={
        'console_scripts': [
            'shrincols=shrincols.cli:main',
        ]
    },
    classifiers = [],
    download_url = 'https://github.com/thiagolcmelo/desafio-idwall/tree/master/strings/archive/0.1.tar.gz',
    url = 'https://github.com/thiagolcmelo/desafio-idwall/tree/master/strings',
)
