import unittest

from BinarySearch import *


class TestBinarySearch(unittest.TestCase):

    def test_BinarySearchTrue(self):
        value = BinarySearch.search([-1, 0, 3, 5, 9, 12], 9)
        self.assertEqual(value, 4, "found")

    def test_BinarySearceFalse(self):
        value = BinarySearch.search([-1, 0, 3, 5, 9, 12], 2)
        self.assertEqual(value, -1, "does not exist")


if __name__ == "__main__":
    unittest.main()
