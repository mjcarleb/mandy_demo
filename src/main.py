import os, sys

# Remove /home/mjcarleb/mandy_demo from sys.path
path = sys.path
print(path[1])
nl = [sys.path[0]]
nl.append(sys.path[2:])
sys.path = nl
print(sys.path)

from my_numpy.Array import my_ndarray as mnp
a = mnp(l=[1, 2, 3, 4, 5])
print(f"The shape of our mnp = {a.shape()}")
print(f"current directory = {os.getcwd()}")
print(f"current path = {sys.path}")
