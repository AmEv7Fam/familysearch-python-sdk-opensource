from distutils.core import setup

import familysearch

setup(
  name = 'familysearch-python-sdk-opensource',
  packages = ['familysearch-python-sdk-opensource'],
  version = familysearch.__version__,
  description = 'A Python SDK for FamilySearch.org',
  long_description=open('README.md').read()
  author = 'Elder Evans',
  author_email = 'elderamevans@gmail.com',
  url = 'https://github.com/elderamevans/familysearch-python-sdk-opensource',
  download_url = 'https://github.com/peterldowns/mypackage/tarball/0.1', 
  keywords = ['FamilySearch', 'API', 'REST', 'family history', 'geneaolgy', 'JSON'] #
  classifiers = [
    "Development Status :: 4 - Beta",
    "Environment :: Console",
    "Environment :: MacOS X",
    "Environment :: Web Environment",
    "Environment :: Win32 (MS Windows)",
    "Environment :: X11 Applications",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.2",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Topic :: Internet :: WWW/HTTP",
    "Topic :: Sociology :: Genealogy",
    "Topic :: Software Development :: Libraries :: Python Modules"
  ],
)
