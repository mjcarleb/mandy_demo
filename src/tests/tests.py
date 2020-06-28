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