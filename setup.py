from setuptools import setup, find_packages

import openflow

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='fpgaopenflow',
    version=openflow.__version__,
    description='a Python library, and CLI utilities, which solves HDL-to-bitstream based on FOSS',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Rodrigo A. Melo',
    author_email='rodrigomelo9@gmail.com',
    license='GPLv3',
    url='https://github.com/PyFPGA/openflow',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'openflow_syn = openflow.helpers.synthesis:main',
            'openflow_imp = openflow.helpers.implementation:main',
            'openflow_bit = openflow.helpers.bitstream:main'
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Utilities',
        'Topic :: Software Development :: Build Tools',
        "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)"
    ]
)
