from enumerable import Enumerable
import unittest


class EnumerableTakeTests(unittest.TestCase):
    def test_take_range_some_items(self):
        e = Enumerable(range(10))
        result = list(e.take(5))
        expected_result = [0, 1, 2, 3, 4]
        self.assertListEqual(result, expected_result)

    def test_take_range_0_items(self):
        e = Enumerable(range(10))
        result = list(e.take(0))
        expected_result = []
        self.assertListEqual(result, expected_result)

    def test_take_range_all_items(self):
        e = Enumerable(range(10))
        result = list(e.take(10))
        expected_result = list(range(10))
        self.assertListEqual(result, expected_result)

    def test_take_range_more_items(self):
        e = Enumerable(range(10))
        result = list(e.take(15))
        expected_result = list(range(10))
        self.assertListEqual(result, expected_result)

    def test_take_dict_some_items(self):
        d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        e = Enumerable(d)
        result = sorted(list(e.take(3)))
        expected_result = ['a', 'b', 'c']
        self.assertListEqual(result, expected_result)

    def test_take_dict_0_items(self):
        d = {'a': 1, 'b': 2}
        e = Enumerable(d)
        result = list(e.take(0))
        expected_result = []
        self.assertListEqual(result, expected_result)

    def test_take_dict_all_items(self):
        d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        e = Enumerable(d)
        result = sorted(list(e.take(4)))
        expected_result = ['a', 'b', 'c', 'd']
        self.assertListEqual(result, expected_result)

    def test_take_dict_more_items(self):
        d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        e = Enumerable(d)
        result = sorted(list(e.take(15)))
        expected_result = ['a', 'b', 'c', 'd']
        self.assertListEqual(result, expected_result)

    def test_take_negative_number_of_items(self):
        l = [1, 2, 3, 'a']
        e = Enumerable(l)
        result = list(e.take(-10))
        expected_result = []
        self.assertListEqual(result, expected_result)

    def test_take_empty(self):
        e = Enumerable.empty()
        result = list(e.take(3))
        expected_result = []
        self.assertListEqual(result, expected_result)
