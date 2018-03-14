from enumerable import Enumerable
import unittest


class EnumerableFirstTests(unittest.TestCase):
    def test_first_range_no_predicate(self):
        e = Enumerable(range(10))
        result = e.first()
        self.assertEqual(result, 0)

    def test_first_range_predicate_exists(self):
        e = Enumerable(range(10))
        result = e.first(lambda x: x > 6)
        self.assertEqual(result, 7)

    def test_first_range_predicate_no_match(self):
        e = Enumerable(range(10))
        result = e.first(lambda x: x == 'hello')
        self.assertIsNone(result)

    def test_first_range_predicate_no_match_default(self):
        e = Enumerable(range(10))
        result = e.first(lambda x: x == 'hello', default=False)
        self.assertFalse(result)

    def test_first_dict_no_predicate(self):
        d = {'a': 1, 'b': 2}
        e = Enumerable(d)
        result = e.first()
        self.assertIn(result, d.keys())

    def test_first_dict_predicate_exists(self):
        d = {'a': 1, 'b': 2}
        e = Enumerable(d)
        result = e.first(lambda x: x != 'a')
        self.assertEqual(result, 'b')

    def test_first_dict_predicate_not_exists(self):
        d = {'a': 1, 'b': 2}
        e = Enumerable(d)
        result = e.first(lambda x: x > 'z')
        self.assertIsNone(result)

    def test_first_dict_empty(self):
        d = dict()
        e = Enumerable(d)
        result = e.first()
        self.assertIsNone(result)

    def test_first_empty_no_predicate(self):
        e = Enumerable.empty()
        result = e.first()
        self.assertIsNone(result)

    def test_first_empty_predicate(self):
        e = Enumerable.empty()
        result = e.first(lambda x: len(x))
        self.assertIsNone(result)
