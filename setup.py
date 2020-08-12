from setuptools import setup
import glob
import os

ver = '0.9.0'

# Generate a __version__.py file with this version in it
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'SNAP_control', '__version__.py'), 'w') as fh:
    fh.write('__version__ = "%s"' % ver)

setup(name='SNAP_control',
      version='%s' % ver,
      description='Python libraries and scripts to control DSA-110 SNAPs',
      author='Rick Hobbs, Vikram Ravi',
      author_email='vikram@caltech.edu',
      url='https://github.com/dsa110/SNAP_control',
      packages = ['SNAP_control'],
      package_data = {'SNAP_control': ['config/*'],},
      scripts=glob.glob('scripts/*.py'),
      )
