import unittest

from SlidingWindow import *


class TestSlideWindow(unittest.TestCase):

    def test_MaxProfit(self):
        value = SlidingWindow.maxProfit([7, 1, 5, 3, 6, 4])
        self.assertEqual(value, 5, "max profit")

    def test_NoProfit(self):
        value = SlidingWindow.maxProfit([7, 6, 4, 3, 1])
        self.assertEqual(value, 0, "zero profit")


if __name__ == "__main__":
    unittest.main()
