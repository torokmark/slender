from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='dast',
      version='0.1.3.3',
      description='DAtaSTructures in Python',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='http://github.com/torokmark/dast',
      author='Mark Torok',
      license='Apache License 2.0',
      packages=['dast'],
      test_suite='nose.collector',
      tests_require=['nose'],
      python_requires='>=3.5',
      entry_points = {
          'console_scripts': ['dast-bin=dast.command_line:main'],
      },
      classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
      ],
      project_urls={
        'Documentation': 'https://dast.readthedocs.io',
        'Source': 'https://github.com/torokmark/dast',
      }
    )
