from setuptools import setup

setup(name='peds',
      version='0.1',
      description='Python Enhanced DataStructures',
      url='http://github.com/torokmark/peds',
      author='Mark Torok',
      license='Apache License 2.0',
      packages=['peds'],
      test_suite='nose.collector',
      tests_require=['nose'],
      entry_points = {
          'console_scripts': ['peds-bin=peds.command_line:main'],
      },
      zip_safe=False)
