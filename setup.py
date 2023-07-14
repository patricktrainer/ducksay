from setuptools import setup, find_packages

setup(
    name='ducksay',
    author='Patrick Trainer',
    author_email='patrick@patricktrainer.xyz',
    version='0.1.0',
    description='A Python implementation of cowsay, but with a duck.',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ducksay = ducksay.ducksay:main',
        ],
    },
)
