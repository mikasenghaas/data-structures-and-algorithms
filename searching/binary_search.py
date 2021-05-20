# binary search symbol table implementation in python

class BinarySearchDict:
    def __init__(self):
        """Initializes an empty symbol table with the specified initial
        capacity.
        :param capacity: the maximum capacity
        """
        self.keys = [None]
        self.vals = [None]
        self.n = 0

    def size(self):
        return self.n

    def __len__(self):
        return self.size()

    def is_empty(self):
        return self.size() == 0

    def contains(self, key):
        if key is None:
            raise ValueError("argument to contains() is None")
        return self.get(key) is not None

    def rank(self, key):
        if key is None:
            raise ValueError("argument to rank() is None")

        lo = 0
        hi = self.n - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if key < self.keys[mid]:
                hi = mid - 1
            elif key > self.keys[mid]:
                lo = mid + 1
            else:
                return mid
        return lo

    def get(self, key):
        if key is None:
            raise ValueError("argument to get() is None")
        if self.is_empty():
            return None
        i = self.rank(key)
        if i < self.n and self.keys[i] == key:
            return self.vals[i]
        return None

    def put(self, key, val):
        if key is None:
            raise ValueError("first argument to put() is None")

        if val is None:
            self.delete(key)
            return

        i = self.rank(key)

        # key is already in table
        if i < self.n and self.keys[i] == key:
            self.vals[i] = val
            return

        # insert new key-value pair
        if self.n == len(self.keys):
            self._resize(2 * len(self.keys))

        j = self.n
        while j > i:
            self.keys[j] = self.keys[j - 1]
            self.vals[j] = self.vals[j - 1]
            j -= 1

        self.keys[i] = key
        self.vals[i] = val
        self.n += 1

    def delete(self, key):
        if key is None:
            raise ValueError("argument to delete() is None")
        if self.is_empty():
            return

        # compute rank
        i = self.rank(key)
        n = self.n

        # key not in table
        if i == n or self.keys[i] != key:
            return

        j = i
        while j < self.n - 1:
            self.keys[j] = self.keys[j + 1]
            self.vals[j] = self.vals[j + 1]
            j += 1

        self.n -= 1
        n = self.n
        self.keys[n] = None  # to avoid loitering
        self.vals[n] = None

        # resize if 1/4 full
        if n > 0 and n == len(self.keys) // 4:
            self._resize(len(self.keys) // 2)

    def delete_min(self):
        if self.is_empty():
            raise ValueError("Symbol table underflow error")
        self.delete(self.min())

    def delete_max(self):
        if self.is_empty():
            raise ValueError("Symbol table underflow error")
        self.delete(self.max())

    def _resize(self, capacity):
        # resize the underlying "arrays"
        assert capacity >= self.n
        tempk = [None] * capacity
        tempv = [None] * capacity
        for i in range(self.n):
            tempk[i] = self.keys[i]
            tempv[i] = self.vals[i]

        self.vals = tempv
        self.keys = tempk

    def min(self):
        if self.is_empty():
            raise ValueError("called min() with empty symbol table")
        return self.keys[0]

    def max(self):
        if self.is_empty():
            raise ValueError("called max() with empty symbol table")
        return self.keys[self.n - 1]

    def floor(self, key):
        if key is None:
            raise ValueError("argument to floor() is None")
        i = self.rank(key)
        if i < self.n and key == self.keys[i]:
            return self.keys[i]
        if i == 0:
            return None
        else:
            return self.keys[i - 1]

    def ceiling(self, key):
        if key is None:
            raise ValueError("argument to ceiling() is None")
        i = self.rank(key)
        if i == self.n:
            return None
        else:
            return self.keys[i]

    def __str__(self):
        string = '{'
        for i in range(self.n):
            string += f'{self.keys[i]} : {self.vals[i]}, '
        return string[:-2] + '}'


if __name__ == '__main__':
    dictionary = BinarySearchDict()

    dictionary.put('name', 'mika')
    dictionary.put('age', 19)
    dictionary.put('name', 'louis')

    print(dictionary)
    print(dictionary.delete_min())
    print(dictionary)
