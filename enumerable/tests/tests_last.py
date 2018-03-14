from enumerable import Enumerable
import unittest


class EnumerableLastTests(unittest.TestCase):
    def test_last_range_no_predicate(self):
        e = Enumerable(range(10))
        result = e.last()
        self.assertEqual(result, 9)

    def test_last_range_predicate_exists(self):
        e = Enumerable(range(10))
        result = e.last(lambda x: x < 6)
        self.assertEqual(result, 5)

    def test_last_range_predicate_no_match(self):
        e = Enumerable(range(10))
        result = e.last(lambda x: x == 'hello')
        self.assertIsNone(result)

    def test_last_range_predicate_no_match_default(self):
        e = Enumerable(range(10))
        result = e.last(lambda x: x == 'hello', default=False)
        self.assertFalse(result)

    def test_last_dict_no_predicate(self):
        d = {'a': 1, 'b': 2}
        e = Enumerable(d)
        result = e.last()
        self.assertIn(result, d.keys())

    def test_last_dict_predicate_exists(self):
        d = {'a': 1, 'b': 2}
        e = Enumerable(d)
        result = e.last(lambda x: x != 'a')
        self.assertEqual(result, 'b')

    def test_last_dict_predicate_not_exists(self):
        d = {'a': 1, 'b': 2}
        e = Enumerable(d)
        result = e.last(lambda x: x > 'z')
        self.assertIsNone(result)

    def test_last_dict_empty(self):
        d = dict()
        e = Enumerable(d)
        result = e.last()
        self.assertIsNone(result)

    def test_last_empty_no_predicate(self):
        e = Enumerable.empty()
        result = e.last()
        self.assertIsNone(result)

    def test_last_empty_predicate(self):
        e = Enumerable.empty()
        result = e.last(lambda x: len(x))
        self.assertIsNone(result)
