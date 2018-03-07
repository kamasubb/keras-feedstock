#!/usr/bin/env python
from setuptools import setup, find_packages
import versioneer


def main():
    skw = dict(
        name='keras',
        version=versioneer.get_version(),
        description='A package for Deep Neural Network',
        author='Phil Elson',
        author_email='pelson.pub@gmail.com',
        url='https://github.com/keras-team/keras'
#        entry_points=dict(console_scripts=[
#            'feedstocks = conda_smithy.feedstocks:main',
#            'conda-smithy = conda_smithy.cli:main']),
        packages=find_packages(),
        include_package_data=True,
        # As conda-smithy has resources as part of the codebase, it is
        # not zip-safe.
        zip_safe=False,
        cmdclass=versioneer.get_cmdclass(),
#        tests_require=['six'],
#        test_suite='conda_smithy',
    )
    setup(**skw)


if __name__ == '__main__':
    main()
