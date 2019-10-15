from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='slender',
      version='2.0.2',
      description='Slender datastructures in Python for efficient work!',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='http://github.com/torokmark/slender',
      author='Mark Torok',
      license='Apache License 2.0',
      packages=['slender'],
      test_suite='nose.collector',
      tests_require=['nose', 'mypy'],
      python_requires='>=3.7',
      entry_points = {
          'console_scripts': ['slender-bin=slender.command_line:main'],
      },
      classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
      ],
      project_urls={
        'Documentation': 'https://slender.readthedocs.io',
        'Source': 'https://github.com/torokmark/slender',
      }
    )
