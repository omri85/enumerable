from itertools import takewhile, dropwhile, islice
from collections import defaultdict
from .group import Group


class Enumerable:
    def __init__(self, iterable):
        self._iter = iter(iterable)

    def __iter__(self):
        return self._iter

    def __next__(self):
        return next(self._iter)

    def count(self, predicate=lambda x: True):
        """Returns the number of items which satisfy the predicate"""
        return sum(1 for item in self if predicate(item))

    def first(self, predicate=lambda x: True, default=None):
        """Returns the first item which satisfies the predicate if any,
        default otherwise"""
        return next((item for item in self if predicate(item)), default)

    def last(self, predicate=lambda x: True, default=None):
        """Returns the last item which satisfies the predicate if any, default
        otherwise"""
        result = default
        for item in (y for y in self if predicate(y)):
            result = item
        return result

    def single(self, predicate=lambda x: True):
        """Returns the first item which satisfies the predicate and asserts
        than exactly one item does."""
        filtered = filter(predicate, self)
        try:
            result = next(filtered)
            try:
                next(filtered)
                raise ValueError("More than one item in sequence") from None
            except StopIteration:
                return result
        except StopIteration:
            raise ValueError("Empty sequence") from None

    def any(self, predicate=lambda x: True):
        """Returns true if at least one item satisfies the predicate, false
        otherwise"""
        return any(True for item in self if predicate(item))

    def all(self, predicate):
        """Returns true all items satisfy the predicate, false otherwise"""
        return all(False for item in self if not predicate(item))

    def sum(self, selector=lambda x: x):
        """Returns the sum of the items according to the selector function"""
        return sum(selector(item) for item in self)

    def avg(self, selector=lambda x: x):
        """Returns the average of the items according to the selector
        function"""
        count = 0
        total = 0
        for item in self:
            count += 1
            total += selector(item)
        if not count:
            raise ValueError("Empty sequence") from None
        return total / count

    def max(self, selector=lambda x: x):
        """Returns the maximal item according to the selector function"""
        try:
            max_item = next(self)
            for item in self:
                if selector(item) > selector(max_item):
                    max_item = item
            return max_item
        except StopIteration:
            raise ValueError("Empty sequence") from None

    def min(self, selector=lambda x: x):
        """Returns the minimal item according to the selector function"""
        try:
            min_item = next(self)
            for item in self:
                if selector(item) < selector(min_item):
                    min_item = item
            return min_item
        except StopIteration as e:
            raise ValueError("Empty sequence") from None

    def select_many(self, selector=lambda x: x):
        """Flattens the collection of collection to on collections"""
        def gen():
            for sub_collection in self:
                yield from selector(sub_collection)
        return Enumerable(gen())

    def where(self, predicate=None):
        """Filters out all the items which do not satisfy the predicate"""
        return Enumerable(filter(predicate, self))

    def select(self, projector):
        """Maps every item according to the projector function"""
        return Enumerable(map(projector, self))

    def take(self, count):
        """Takes only n items (or less if less items exist)"""
        count = max(count, 0)
        return Enumerable(islice(self, count))

    def skip(self, count):
        """Skips n items (or less if less items exist)"""
        count = max(count, 0)
        return Enumerable(islice(self, count, None))

    def take_while(self, predicate):
        """Takes items as long as the predicate satisfies"""
        return Enumerable(takewhile(predicate, self))

    def skip_while(self, predicate):
        """Skips items as long as the predicate satisfies"""
        return Enumerable(dropwhile(predicate, self))

    def group_by(self, key_selector):
        """Groups the items in the collection according to the key selector
        function"""
        def gen():
            groups = defaultdict(list)
            for item in self:
                key = key_selector(item)
                groups[key].append(item)
            for key, value in groups.items():
                yield Group(key, Enumerable(value))
        return Enumerable(gen())

    def to_list(self):
        """Enumerates the collection to a list"""
        return list(self)

    def to_dict(self, key_func, value_func):
        """Enumerates to collection to a dictionary according to the key and
        value functions"""
        return {key_func(item): value_func(item) for item in self}

    @staticmethod
    def empty():
        def gen():
            return
            yield
        return Enumerable(gen())
