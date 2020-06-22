from setuptools import find_packages, setup

setup(
   name='my_numpy',
   version='1.0',
   description='Learning to create packages mimicing numpy',
   author='Mark Carlebach',
   author_email='markjcarelbach@gmail.com',
   packages=['my_numpy'],  #same as name
   install_requires=['numpy', 'pandas'], #external packages as dependencies
)
