"""
We are using default Python built-in unittest framework (see definition of test runner here)
- https://realpython.com/pytest-python-testing/

There is also pytest framework (alternative to unittest)
- https://realpython.com/pytest-python-testing/
- https://www.slant.co/versus/9148/9149/~unittest_vs_pytest
- https://pythontesting.net/framework/pytest/pytest-introduction/
- https://pythontesting.net/framework/pytest/pytest-introduction/#discovery

NOTE:  In pytest, I found "discovery" of tests to be confusing.   It all has to do with directory structure, naming
       conventions, where you run tests from, etc.  The 2nd link above explains pretty well.

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