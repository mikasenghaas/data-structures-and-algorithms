# hash table implementation in python using separate chaining
from itu.algs4.searching.sequential_search_st import SequentialSearchST


class SeparateChainingHashST:
    def __init__(self, M=997):
        self.m = M  # hash table size
        self.n = 0  # number of pairs
        self.st = [SequentialSearchST()
                   for _ in range(0, M)]  # Array of ST objects

    def size(self):
        return self.n

    def is_empty(self):
        return self.n == 0

    @staticmethod
    def _hash(key, m):
        # Hash value between 0 and M-1
        return (hash(key) & 0x7FFFFFFF) % m

    def get(self, key):
        if key is None:
            raise ValueError("argument to get() is None")
        i = self._hash(key, self.m)
        return self.st[i].get(key)

    def put(self, key, value):
        if key is None:
            raise ValueError("first argument to put() is None")
        if value is None:
            self.delete(key)
            return
        i = self._hash(key, self.m)
        print(i)
        if not self.st[i].contains(key):
            self.n += 1
        self.st[i].put(key, value)
        self.st[self._hash(key, self.m)].put(key, value)

    def contains(self, key):
        if key is None:
            raise ValueError("argument to contains() is None")
        return self.get(key) is not None

    def delete(self, key):
        if key is None:
            raise ValueError("argument to delete() is None")
        i = self._hash(key, self.m)
        if self.st[i].contains(key):
            self.n -= 1
        self.st[i].delete(key)

    def keys(self):
        keys = []
        for i in range(0, self.m):
            for key in self.st[i].keys():
                keys.append(key)
        return keys

    def __len__(self):
        return self.size()


if __name__ == '__main__':
    dictionary = SeparateChainingHashST()
    dictionary.put('name', 'mika')
    dictionary.put('age', 19)

    print(dictionary.get('age'))
    print(dictionary.keys())
