import unittest
from circles import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # Test area when radius >= 0
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi*2.1**2)

    def test_values(self):
        # Raise value errors when bad inputs
        self.assertRaises(ValueError, circle_area, -2)
    