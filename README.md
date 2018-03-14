What is enumerable?
-------------------
## .NET LINQ for Python
__Enumerable__ is a module that combines the power of generators with the elegance of functional programming to allow easy and efficient work with large collections.
__Enumerable__ is a generator based class, which have a set of functions that allow lazy projection and filtering that will only be executed once.

# Example:
Suppose we have a big collection of people and their grades and we want to work with that data, here's a small example:

```python
    my_data = [{'name': 'Lyn', 'gender': 'female', 'age': 24, 'grades': [90, 70, 80]},
               {'name': 'Dor', 'gender': 'male', 'age': 30, 'grades': [60, 81]},
               {'name': 'Rav', 'gender': 'female', 'age': 32, 'grades': [50, 42]},...]
```
**Notice:** `Enumerable` object can be created from every object which has an iterator: file, csv-reader, list, set...
```python
    from enumerable import Enumerable
    enumerable = Enumerable(iterable)
```

Now let's say we want the average age of all the women:
```python
    avg_age = Enumerable(my_data).where(lambda x: x['gender']=='female').avg(lambda x: x['age'])
```

The maximum grade a student under 30 got:
```python
    max_grade = Enumerable(my_data).where(lambda x: x['age']<30).select_many(lambda x: x['grades']).max()
```

The names of 5 students who has at least one grade equals to 100:
```python
    result = Enumerable(my_data).where(lambda x: Enumerable(x['grades']).any(lambda y: y==100)).take(5).select(lambda x: x['name'])
```
**Notice**: no operation took place since all of those functions return `Enumerable` object.
The items will be evaluated and the chain will be executed only once the collection is materialized:
```python
    list(result)
    set(result)
    [item for item in result]
    ...
```

#### Lazy evaluation functions (return Enumerable):
- `count([predicate=lambda x: True])` - counts the items in the collection which satisfies the predicate.
- `select(selector)` - maps every item to the select function values.
- `where(predicate)` - filters out items which do not satisfy the predicate.
- `select_many([select_func=lambda x: x])` - flattens the collection of collections to one collection.
- `take(n)` - takes only n items (or less if less items exist).
- `take_while(predicate)` - takes all the items as long as the predicate satisfies
- `skip(n)` - skips n items (or less if less items exist).
- `skip_while(predicate)` - skips the items as long as the predicate satisfies
- `group_by(key_selector)` - returns Group objects which which contains keys and Enumerable objects of items which all yielded the same key.

**Notice:** These functions return a new `Enumerable`. __No__ item is evaluated.

#### Aggregation functions (return scalar):
- `first([predicate=lambda x: True], [default=None])` - returns the first item that satisfies the predicate if any, and `default` otherwise.
- `last([predicate=lambda x: True], [default=None])` - returns the last item that satisfies the predicate if any, and `default` otherwise.
- `single([predicate=lambda x: True])` - return the first item that satisfies the predicate. If none or more than one item does, a `ValueError` exception will be raised.
- `any([predicate=lambda x: True])` - returns `True` if at least one item exists or at least one item satisfies the predicate. `False` otherwise.
- `all(predicate)` - returns `True` if all items satisfy the predicate or if no item exists. `False` otherwise.
- `max([select_func])` - returns the maximal item or the item with the maximum value according to the `select_func`. If no item exists, a `ValueError` exception will be raised.
- `min([select_func])` - returns the minimal item or the item with the minimum value according to the `select_func`.  If no item exists, a `ValueError` exception will be raised.
- `avg([select_func])` - returns the average of all items or of all values according to the `select_func`.  If no item exists, a `ValueError` exception will be raised.
- `sum([select_func])` - returns the sum of all items or of all values according to the `select_func`. 0 if no items exists.

**Notice:** These functions cause evaluation of the items in the collections.

#### Enumeration functions (materialize the collection):
- `to_list()` - returns a list with the elements in the collection. Equals to `list(enumerable_object)`
- `to_dict(key_func, value_func)` - returns a dictionary from the items in the collection. The keys and values are the outcome of the function, respectively.