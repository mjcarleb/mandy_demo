from my_numpy.Array import my_ndarray as mnp
a = mnp(l=[1, 2, 3, 4, 5])
print(f"The shape of our mnp = {a.shape()}")
print()

import os, sys

# Remove /home/mjcarleb/mandy_demo from sys.path
path = sys.path
print("Sys Path:")
print(sys.path)
print()
print("Current Directory:")
print(os.getcwd())