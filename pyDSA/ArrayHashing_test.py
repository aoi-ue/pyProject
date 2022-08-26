import unittest

from ArrayHashing import *

class TestAnagram(unittest.TestCase):

    def test_isAnagram(self):
        passed_test_cases = [
            ['anagram', 'nagaram', True], 
            ['banana', 'ananba', True], 
            ['cat', 'rat', False], 
            ['capoo', 'pooca', True], 
            ['mekbuk', 'mekpro', False]
        ]
        for s1, s2, expected in passed_test_cases: 
            with self.subTest(s1=s1, s2=s2):
                isAnagram = ArrayHashing.isAnagram(s1, s2)
                self.assertEqual(isAnagram, expected, 'should return result as intended')

class TestTwoSum(unittest.TestCase):

    def test_firstSum(self):
        value = ArrayHashing.twoSum([2, 7, 11, 15], 9)
        self.assertEqual(value, [0, 1], 'correct sum')

    def test_firstWrongSum(self):
        value = ArrayHashing.twoSum([2, 7, 11, 15], 9)
        self.assertNotEqual(value, [0, 2], 'wrong sum')

class TestDuplicated(unittest.TestCase):
    def test_duplicated(self):
        self.assertTrue(ArrayHashing.containsDuplicate([2, 2, 2]))

    def test_non_duplicated(self):
        self.assertFalse(ArrayHashing.containsDuplicate([2, 7, 11, 15]))

if __name__ == '__main__':
    unittest.main()
