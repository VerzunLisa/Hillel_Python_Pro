class CustomColl(object):
    def __init__(self, a):
        """Initialization data"""
        self.a = a

    def __len__(self):
        """The number of elements"""
        return len(self.a)

    def __iter__(self):
        """Iterator"""
        return iter(self.a)

    def __getitem__(self, item):
        """Gets an element by index"""
        return self.a[item]


def my_len(collection):
    """My function the number of elements"""
    count = 0
    for x in collection:
        count += 1
    return count


def my_sum(collection):
    """My function sum"""
    total = 0
    for item in collection:
        total += item
    return total


def my_minimal(collection):
    """My function minimal number"""
    iterat = iter(collection)
    minimal = next(iterat)

    for item in iterat:
        if item < minimal:
            minimal = item
    return minimal


def testing():
    """Testing functions my_len, my_sum, my_minimal"""
    collection = CustomColl([3, 4, 2, 8, 15])
    print(my_len(collection))
    print(my_sum(collection))
    print(my_minimal(collection))


testing()
