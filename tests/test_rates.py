import unittest

from warehouse.rates import shipping_quote


class RateTests(unittest.TestCase):
    def test_standard_rates(self):
        self.assertEqual(shipping_quote(2, "local"), 8.0)
        self.assertEqual(shipping_quote(2, "regional"), 11.0)

    def test_local_rates_across_weights(self):
        for weight, expected in [(0.5, 5.75), (1, 6.5), (3, 9.5), (1.234, 6.85)]:
            with self.subTest(weight=weight):
                self.assertEqual(shipping_quote(weight, "local"), expected)

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local")
