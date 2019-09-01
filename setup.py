#!/usr/bin/env python3

from setuptools import setup

setup(
    name="stegsuite",
    version="0.0.0a1",
    url="https://github.com/WHGhost/stegSUITE", #TODO Update with actual real page
    description='A library and tools to do some cool stego!',
    long_description="""A Collection of tools to do some stego""",
    author='WHGhost',
    author_email='wghosth@gmail.com',
    license='GPL-3.0',
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 3',
    ],
    keywords='library steganography file analysis ',
    packages=["stegsuite"],
    install_requires=[],
    python_requires='>=3',
    package_data={},
    data_files=[],
)
