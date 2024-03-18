import unittest

from TwoPointers import *


class isPalindrome(unittest.TestCase):
    def test_palindromeTrue(self):
        self.assertTrue(TwoPointers.isPalindrome("A man, a plan, a canal: Panama"))

    def test_palindromeFalse(self):
        self.assertFalse(TwoPointers.isPalindrome("race a car"))

    def test_palindromeEmpty(self):
        self.assertTrue(TwoPointers.isPalindrome(" "))


if __name__ == "__main__":
    unittest.main()
