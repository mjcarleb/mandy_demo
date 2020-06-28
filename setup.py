from setuptools import find_packages, setup

"""
See these links for more about modules, packages and distributions (including setup.py): 
   - https://packaging.python.org/tutorials/packaging-projects/ 
   - https://docs.python.org/3/distutils/setupscript.html
   - https://www.tutorialsteacher.com/python/python-package
   
Steps to create and install local package to import as you would true open source software:
1.  Create parent directory for package(s) anywhere
2.  Create package directory anywhere (with __init__, which might no longer be necessary?)
3.  Inside package directory, create .py modules with functions and classes that belong to the package
4.  Inside parent directory (same level as package(s)), create setup.py
5.  In setup.py, name the package, requirements, etc.
6.  See link above for more options when creating setup.py (e.g., multiple packages, variations on directory structure)
7.  From command line while in environment and in parent directory with setup.py, type $pip install -e .   
8.  The above copies/links into environment site packages (see my-numpy.egg-link)
9.  Try $pip uninstall my_numpy to reverse the above link
10.  While in environment, you can import like you would a real package (e.g., import numpy as np, etc.)

NOTE:  Other option (less elegant that above), just add path to package directory to sys.path (either inside python
       code or by changing environment variable for $PATH
       
TBD:  tests folder should be at same level as setup.py...need to explore how to get unit tests to be part of package
"""
setup(
   name='my_numpy',
   version='1.0',
   description='Learning to create packages mimicing numpy',
   author='Mark Carlebach',
   author_email='markjcarelbach@gmail.com',
   packages=['my_numpy'],  #same as name
   install_requires=['numpy', 'pandas'], #external packages as dependencies
)
