from enumerable import Enumerable
import unittest


class EnumerableAllTests(unittest.TestCase):
    def test_all_range_some_false(self):
        e = Enumerable(range(10))
        result = e.all(lambda x: x < 9)
        self.assertFalse(result)

    def test_all_range_all_false(self):
        e = Enumerable(range(10))
        result = e.all(lambda x: x == '1')
        self.assertFalse(result)

    def test_all_range_all_true(self):
        e = Enumerable(range(10))
        result = e.all(lambda x: x < 100)
        self.assertTrue(result)

    def test_all_dict_some_false(self):
        d = {'a': 1, 'b': 2}
        e = Enumerable(d)
        result = e.all(lambda x: x < 'b')
        self.assertFalse(result)

    def test_all_dict_all_false(self):
        d = {'a': 1, 'b': 2}
        e = Enumerable(d)
        result = e.all(lambda x: x > 'b')
        self.assertFalse(result)

    def test_all_dict_all_true(self):
        d = {'a': 1, 'b': 2}
        e = Enumerable(d)
        result = e.all(lambda x: x.isalpha())
        self.assertTrue(result)

    def test_all_dict_empty(self):
        d = dict()
        e = Enumerable(d)
        result = e.all(lambda x: True)
        self.assertTrue(result)

    def test_all_empty(self):
        e = Enumerable.empty()
        result = e.all(lambda x: False)
        self.assertTrue(result)
