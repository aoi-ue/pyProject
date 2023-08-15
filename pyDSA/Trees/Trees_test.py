import unittest

from Trees import BinaryTree

class TestTree(unittest.TestCase):

    def test_TreeInit(self):
        tree = BinaryTree()
        for i in range(10):
            tree.add((i))

        tree.printTree("in-order")
        
        self.assertFalse(False, 'default False')

if __name__ == '__main__':
    unittest.main()
