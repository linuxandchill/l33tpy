import unittest
from sorty import sort

class TestSort(unittest.TestCase):
    def test_sort(self):
        self.assertEqual(sort([5, 66, 4, 1, 3]), [1, 3, 4, 5, 66])
