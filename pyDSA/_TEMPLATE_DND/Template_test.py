import unittest

from Template import *


class isTemplating(unittest.TestCase):
    def test_palindromeTrue(self):
        self.assertTrue(Template.Templating("Testing"))


if __name__ == "__main__":
    unittest.main()
