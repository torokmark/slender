from setuptools import setup

setup(name='dast',
      version='0.1',
      description='DAtaSTructures in Python',
      url='http://github.com/torokmark/dast',
      author='Mark Torok',
      license='Apache License 2.0',
      packages=['dast'],
      test_suite='nose.collector',
      tests_require=['nose'],
      entry_points = {
          'console_scripts': ['dast-bin=dast.command_line:main'],
      },
      zip_safe=False)
