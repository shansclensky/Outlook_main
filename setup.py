from setuptools import setup, find_packages

setup(
    name='Outlook Test Framework',
    packages=find_packages(),
    install_requires=[x.strip() for x in open('requirements.txt').readlines()],
    version='0.0.1',
    description='UI Testing Framework',
    author='n',
    author_email='',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',

    ]
)