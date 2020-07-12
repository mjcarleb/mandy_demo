"""
We are using default Python built-in unittest framework (see definition of test runner here)
- https://docs.python.org/3/library/unittest.html

There is also pytest framework (alternative to unittest)
- https://realpython.com/pytest-python-testing/
- https://pythontesting.net/framework/pytest/pytest-introduction/
- https://pythontesting.net/framework/pytest/pytest-introduction/#discovery
- https://docs.pytest.org/en/stable/goodpractices.html
- https://docs.pytest.org/en/stable/example/pythoncollection.html
- https://docs.pytest.org/en/stable/customize.html

NOTE:  In pytest, I found "discovery" of tests to be confusing.   It all has to do with directory structure, naming
       conventions, where you run tests from, etc.  Many of the links above attempt to explain the complex protocol
       with myriads of optionality/complexity (e.g., parameters specified in any ".ini" file (e.g., tox.ini).

       Finding the rootdir (from https://docs.pytest.org/en/stable/customize.html):
            Here is the algorithm which finds the rootdir from args:

                -determine the common ancestor directory for the specified args that are recognised as paths that exist in the file system. If no such paths are found, the common ancestor directory is set to the current working directory.
                -look for pytest.ini, tox.ini and setup.cfg files in the ancestor directory and upwards. If one is matched, it becomes the ini-file and its directory becomes the rootdir.
                -if no ini-file was found, look for setup.py upwards from the common ancestor directory to determine the rootdir.
                -if no setup.py was found, look for pytest.ini, tox.ini and setup.cfg in each of the specified args and upwards. If one is matched, it becomes the ini-file and its directory becomes the rootdir.
                -if no ini-file was found, use the already determined common ancestor as root directory. This allows the use of pytest in structures that are not part of a package and don’t have any particular ini-file configuration.
                -If no args are given, pytest collects test below the current working directory and also starts determining the rootdir from there.

"""
import unittest
from my_numpy.Array import my_ndarray as mnp


class TestArray(unittest.TestCase):

    def test_shape(self):

        # Creating an instance (i.e., object) of our 'my_ndarray' class
        a = mnp(l=[1, 2, 3, 4, 5])

        # Now create positive and negative tests to ensure shape method is working
        self.assertEqual(first=a.shape(), second="[5, 1]")
        self.assertTrue(expr=a.shape() == "[5, 1]")
        self.assertFalse(expr=a.shape() == "[4, 1]")


if __name__ == '__main__':
    unittest.main()