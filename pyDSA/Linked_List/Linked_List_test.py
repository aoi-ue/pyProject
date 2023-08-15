import unittest

from Linked_List import *


class TestSingleLinkedList(unittest.TestCase):
    def test_insertFirst(self):
        llist = LinkedList()
        llist.insert_head("a")
        llist.insert_end("b")
        llist.insert_head("c")
        llist.insert_end("d")
        self.assertEqual(llist.count_elements(), 4, "count correctly")


if __name__ == "__main__":
    unittest.main()
