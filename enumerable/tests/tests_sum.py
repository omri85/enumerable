from enumerable import Enumerable
import unittest


class EnumerableSumTests(unittest.TestCase):
    def test_sum_range_default_selector(self):
        e = Enumerable(range(8))
        result = e.sum()
        self.assertEqual(result, sum(range(8)))

    def test_sum_range_with_selector(self):
        e = Enumerable(range(8))
        result = e.sum(lambda x: 1)
        self.assertEqual(result, 8)
