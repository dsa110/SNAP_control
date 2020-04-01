from distutils.core import setup
import glob
import os

ver = '0.0.1'
try:
    import subprocess
    ver = ver + '-' + subprocess.check_output(['git', 'describe', '--abbrev=8', '--always', '--dirty', '--tags']).strip()
except:
    print('Couldn\'t get version from git. Defaulting to %s' % ver)

# Generate a __version__.py file with this version in it
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'src', '__version__.py'), 'w') as fh:
    fh.write('__version__ = "%s"' % ver)

setup(name='hera_corr_f',
      version='%s' % ver,
      description='Python libraries and scripts to control the HERA correlator F-Engines',
      author='Jack Hickish',
      author_email='jackh@berkeley.edu',
      url='https://github.com/hera-team/hera_corr_f',
      provides=['hera_corr_f'],
      packages=['hera_corr_f'],
      package_dir={'hera_corr_f' : 'src'},
      scripts=glob.glob('scripts/*.py'),
      )

if ver.endswith("dirty"):
    print "********************************************"
    print "* You are installing from a dirty git repo *"
    print "*      One day you will regret this.       *"
    print "*                                          *"
    print "*  Consider cleaning up and reinstalling.  *"
    print "********************************************"
