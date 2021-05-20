# set implementation based on separate chaining hashing
from itu.algs4.fundamentals.bag import Bag


class MyBag(Bag):
    def __init__(self):
        super().__init__()

    def contains(self, item):
        curr = self._first
        while curr is not None:
            if curr.item == item:
                return True
            curr = curr.next
        return False


class Set:
    INITIAL_SIZE = 1000

    def __init__(self):
        self.m = Set.INITIAL_SIZE
        self.n = 0
        self.set = [MyBag()
                    for _ in range(0, self.m)]  # Array of ST objects

    def size(self):
        return self.n

    def __len__(self):
        return self.n

    def add(self, item):
        hash_val = self.hasher(item, self.m)

        if self.set[hash_val].contains(item):
            return
        self.set[hash_val].add(item)
        self.n += 1

    def contains(self, item):
        hash_val = self.hasher(item, self.m)

        return True if self.set[hash_val].contains(item) else False

    def __repr__(self):
        string = '{ '
        for bag in self.set:
            for val in bag:
                string += f'{val} '
        return string + '}'

    @staticmethod
    def hasher(item, m):
        return (hash(item) & 0x7FFFFFFF) % m


if __name__ == '__main__':
    s = Set()
    s.add('Glumanda')
    s.add('Pickachu')
    s.add('Glumanda')
    s.add('Glumanda')
    s.add('Shiggy')
    s.add('Pickachu')
    s.add('Pickachu')

    print(s)
    print(len(s))
