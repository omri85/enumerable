from enumerable import Enumerable
import unittest


class EnumerableAnyTests(unittest.TestCase):
    def test_any_range_some_true(self):
        e = Enumerable(range(10))
        result = e.any(lambda x: x == 9)
        self.assertTrue(result)

    def test_any_range_predicate_not_exists(self):
        e = Enumerable(range(10))
        result = e.any(lambda x: x > 100)
        self.assertFalse(result)

    def test_any_dict_predicate_exists(self):
        d = {'a': 1, 'b': 2}
        e = Enumerable(d)
        result = e.any(lambda x: x.isalpha())
        self.assertTrue(result)

    def test_any_dict_predicate_not_exists(self):
        d = {'a': 1, 'b': 2}
        e = Enumerable(d)
        result = e.any(lambda x: x.isdigit())
        self.assertFalse(result)

    def test_any_dict_empty(self):
        d = dict()
        e = Enumerable(d)
        result = e.any(lambda x: True)
        self.assertFalse(result)

    def test_any_empty(self):
        e = Enumerable.empty()
        result = e.any(lambda x: False)
        self.assertFalse(result)
