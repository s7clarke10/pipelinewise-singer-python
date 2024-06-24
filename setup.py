#!/usr/bin/env python

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name="pipelinewise-singer-python",
      version='3.0.0',
      description="Singer.io utility library - PipelineWise compatible",
      python_requires=">=3.8.0, <3.13",
      long_description=long_description,
      long_description_content_type="text/markdown",
      author="TransferWise",
      classifiers=[
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3 :: Only'
      ],
      url="https://github.com/transferwise/pipelinewise-singer-python",
      install_requires=[
          'pytz>=2018.4',
          'jsonschema>=3.2.0,==3.*',
          'msgspec>=0.18.0',
          'python-dateutil>2.7.3,==2.*',
          'backoff>=2.2.1,==2.*',
          'ciso8601>=2.3.1,==2.*',
      ],
      extras_require={
          'dev': [
              'pylint==3.0.2,==3.*',
              'pytest>=7.1.2,==7.*',
              'coverage[toml]>=6.3,<8.0',
              'ipython',
              'ipdb',
              'unify==0.5'
          ]
      },
      packages=['singer'],
      package_data={
          'singer': [
              'logging.conf'
          ]
      },
      include_package_data=True
      )
