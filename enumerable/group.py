class Group:
    def __init__(self, key, items):
        self.key = key
        self.group = items

    def __iter__(self):
        return self.group

    def __next__(self):
        return next(self.group)
