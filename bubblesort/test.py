import unittest
from index import bubble

class TestBubble(unittest.TestCase):
    def test_empty_array(self):
        # If empty array return []
        self.assertFalse(bubble([]))

    def test_sorts_correctly(self):
        self.assertEqual(bubble([3,4,2,4]), [2,3,4,4])