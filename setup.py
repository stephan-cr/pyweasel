try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name = 'pyweasel',
      version = '0.1',
      author = 'Stephan Creutz',
      packages = ['weasel'],
      scripts = ['scripts/pyweasel.py'],
      url = 'http://bitbucket.org/stephan_cr/pyweasel',
      description = 'finds weasel words in Python class or function names',
      package_data = { 'weasel': ['data/*.dat'] })
