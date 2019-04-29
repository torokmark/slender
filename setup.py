from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='dast',
      version='0.1.3.1',
      description='DAtaSTructures in Python',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='http://github.com/torokmark/dast',
      author='Mark Torok',
      license='Apache License 2.0',
      packages=['dast'],
      python_requires='>3.5.0',
      test_suite='nose.collector',
      tests_require=['nose'],
      entry_points = {
          'console_scripts': ['dast-bin=dast.command_line:main'],
      },
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ]
    )
