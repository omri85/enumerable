from enumerable import Enumerable
import unittest


class EnumerableSelectManyTests(unittest.TestCase):
    def test_select_many_deafult_selector(self):
        e = Enumerable([range(3) for i in range(3)])
        result = e.select_many().to_list()
        self.assertListEqual(result, [0, 1, 2, 0, 1, 2, 0, 1, 2])

    def test_select_many_with_selector(self):
        e = Enumerable([('a', [1, 2]), ('b', [3, 4])])
        result = e.select_many(lambda x: x[1]).to_list()
        self.assertListEqual(result, [1, 2, 3, 4])

    def test_select_many_empty_sub_collections(self):
        e = Enumerable([[], [], {}, (), range(0)])
        result = e.select_many().to_list()
        self.assertListEqual(result, [])

    def test_select_many_empty_list(self):
        e = Enumerable([])
        result = e.select_many().to_list()
        self.assertListEqual(result, [])

    def test_select_many_empty(self):
        e = Enumerable.empty()
        result = e.select_many().to_list()
        self.assertListEqual(result, [])

    def test_select_many_empty_with_predicate(self):
        e = Enumerable.empty()
        result = e.select_many(lambda x: x[0]).to_list()
        self.assertListEqual(result, [])
