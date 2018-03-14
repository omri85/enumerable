from enumerable import Enumerable
import unittest


class EnumerableSelectTests(unittest.TestCase):
    def test_select_to_list(self):
        e = Enumerable(range(5))
        result = e.select(lambda x: x*2).to_list()
        self.assertListEqual(result, [0, 2, 4, 6, 8])

    def test_select_to_dict(self):
        e = Enumerable(range(1, 4))
        result = e.select(lambda x: 'a'*x).to_dict(lambda x: x,
                                                   lambda x: len(x))
        self.assertDictEqual(result, {'a': 1, 'aa': 2, 'aaa': 3})

    def test_select_empty_list(self):
        e = Enumerable([])
        result = e.select(lambda x: 'hello').to_list()
        self.assertListEqual(result, [])

    def test_select_empty(self):
        e = Enumerable.empty()
        result = e.select(lambda x: x/3).to_list()
        self.assertListEqual(result, [])
