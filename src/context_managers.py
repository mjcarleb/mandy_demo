import os

###############
# As object
###############
print("##################################################################################################")
print("####################################### as object ################################################")
print("##################################################################################################")
print()

class change_dir:

    def __init__(self, new_dir):
        self.new_dir = new_dir

    def __enter__(self):
        self.cwd = os.getcwd()
        os.chdir(self.new_dir)

    def __exit__(self, *args):
        os.chdir(self.cwd)

print(f"Outside context manager:  {os.getcwd()}")
print()

with change_dir("../data/external"):
    print(f"Inside context manager:  {os.getcwd()}")
    with open("text.txt") as f:
        lines = f.readlines()
        for line in lines:
            print(line[:-1])
    print()

print(f"Outside context manager:  {os.getcwd()}")

with change_dir("../data/raw"):
    print(f"Inside context manager:  {os.getcwd()}")
    with open("text.txt") as f:
        lines = f.readlines()
        for line in lines:
            print(line[:-1])
    print()

###############
# Now as function using contextmanager decorator
###############
print("##################################################################################################")
print("############################### generator and decorator ##########################################")
print("##################################################################################################")
print()
from contextlib import contextmanager

@contextmanager
def change_dir(new_dir):

    try:
        cwd = os.getcwd()
        os.chdir(new_dir)
        yield
    finally:
        os.chdir(cwd)

print(f"Outside context manager:  {os.getcwd()}")
print()

with change_dir("../data/external"):
    print(f"Inside context manager:  {os.getcwd()}")
    with open("text.txt") as f:
        lines = f.readlines()
        for line in lines:
            print(line[:-1])
    print()

print(f"Outside context manager:  {os.getcwd()}")

with change_dir("../data/raw"):
    print(f"Inside context manager:  {os.getcwd()}")
    with open("text.txt") as f:
        lines = f.readlines()
        for line in lines:
            print(line[:-1])
    print()
