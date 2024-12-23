"""
Sample Test
"""

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Test the Calc module"""

    def test_add_number(self):
        """Test Adding numbers together"""
        res = calc.add(3, 8)
        self.assertEqual(res, 11)

    def test_subtract_number(self):
        """Test Subtracting numbers together"""
        res = calc.subtract(5, 11)
        self.assertEqual(res, 6)
