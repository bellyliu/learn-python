# test_my_app.py

import unittest
from my_app import calculate_price


class TestPriceCalculator(unittest.TestCase):

    def test_basic_price(self):
        self.assertEqual(calculate_price(100, 0.1), 110)

    def test_with_zero_tax(self):
        self.assertEqual(calculate_price(50, 0), 50)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_price(-10, 0.1)


if __name__ == '__main__':
    unittest.main()
