"""
See these links for more about modules, packages and distributions (including setup.py): 
   - https://packaging.python.org/tutorials/packaging-projects/ 
   - https://docs.python.org/3/distutils/setupscript.html
   - https://www.tutorialsteacher.com/python/python-package
   
Steps to create and install local package to import as you would true open source software:

-- parent directory
   -- setup.py
   -- package directory
      -- __init__.py
      -- module1.py
      -- module2. py
   
1.  Create parent directory for package(s) anywhere
2.  Inside parent directory, create package directory (with __init__, which might not be necessary?)
3.  Inside package directory, create .py modules with functions and classes that belong to the package
4.  Inside parent directory (same level as package(s)), create setup.py
5a.  In setup.py, name the package, requirements, etc.
5b.  We have created our distribution at this point (with setup.py in our "parent" or "distribution" directory)
5c.  See link above for more options when creating setup.py (e.g., multiple packages, variations on directory structure)
6.  So now, we install.  Just like we would if we were installing numpy!
    From command line in parent directory with setup.py (while in environment in which you want to install your
    package), installation), type $pip install -e .   
7.  The above adds to your environment's site packages a link to your package (see my-numpy.egg-link)
8.  Try $pip uninstall my_numpy to remove the above link
9.  After install (before uninstall), while you are in the environment, you can import your package just like you
     would a "real" open source software package such as numpy   (NOTE:  This is the goal!)
      
NOTE:  Other option (less elegant that above), just add path to package directory to sys.path (either inside python
       code or by changing environment variable for $PATH)
       
TBD:  tests folder should be at same level as setup.py...need to explore how to get unit tests to be part of package
"""

from setuptools import find_packages, setup
setup(
   name='my_Numpy',
   version='1.0',
   description='Learning to create packages mimicing numpy',
   author='Mark Carlebach',
   author_email='markjcarelbach@gmail.com',
   packages=['my_Numpy'],  #same as name
   install_requires=['numpy', 'pandas'], #external packages as dependencies
)
