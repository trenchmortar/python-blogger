from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='pyblog',
      version=version,
      description="This library provides a pure python interface for the various blogging API.",
      long_description="""\
This library provides a pure python interface for the various blogging API.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Currently, only Metaweblog and Wordpress are implemented but it will be extended to use MovableType? and Blogger soon. Since Blogger has now moved onto GData API, this interface will internally use GData API rather then XML-RPC.Ritesh Nadhani',
      author_email='riteshn@gmail.com',
      url='http://code.google.com/p/python-blogger/',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
