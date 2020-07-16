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

    # Enter happens as 'with" is executed
    def __enter__(self):
        self.cwd = os.getcwd()
        os.chdir(self.new_dir)

    # Exit happens when you leave the with context
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
    # try/finally makes more robust but not necessary

    # Before yield is like __enter__
    try:
        cwd = os.getcwd()
        os.chdir(new_dir)
        yield

    # After  yield is like __exit__
    finally:
        os.chdir(cwd)

@contextmanager
def change_dir(new_dir):

    # Before yield = __enter__
    cwd = os.getcwd()
    os.chdir(new_dir)
    yield

    # After yield = __exit__
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
