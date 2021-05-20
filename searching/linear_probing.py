# hash table implementation in python using linear probing for collision-resolution

class LinearProbingHashST:
    def __init__(self, M=997):
        self.m = M  # hash table size
        self.n = 0  # number of pairs
        self.keys = [None] * self.m
        self.vals = [None] * self.m

    def size(self):
        return self.n

    def is_empty(self):
        return self.n == 0

    @staticmethod
    def _hash(key, m):
        # hash value between 0 and m-1
        # compute hash 32-bit integer hash value, make positive through bitwise operation (could also do math.abs()) and lastly take modulus to obtain array index
        return (hash(key) & 0x7FFFFFFF) % m

    def contains(self, key):
        if key is None:
            raise ValueError("argument to get() is None")
        return self.get(key) != None

    def put(self, key, val):
        if key is None:
            raise ValueError("key argument to get() is None")
        if val is None:
            raise ValueError("value argument to get() is None")
        if val is None:
            self.delete(key)
            return

        # resize if table is 50% full
        if self.n >= self.m // 2:
            self._resize(2 * self.m)

        hash_val = self._hash(key, self.m)

        while self.keys[hash_val] is not None:
            if self.keys[hash_val] == key:
                self.vals[hash_val] = val
                return
            hash_val = (hash_val + 1) % self.m
        self.keys[i] = key
        self.vals[i] = val
        self.n += 1

    def get(self, key):
        if key is None:
            raise ValueError("argument to get() is None")

        hash_val = self._hash(key, self.m)

        while self.keys[hash_val] is not None:
            if self.keys[hash_val] == key:
                return self.vals[hash_val]
            hash_val = (hash_val + 1) % self.m
        return None

    def delete(self, key):
        if key is None:
            raise ValueError("argument to delete() is None")
        if not self.contains(key):
            return
        # Find position i of key
        i = self._hash(key, self.m)
        while not key == self.keys[i]:
            i = (i + 1) % self.m
        # Delete key and associated value
        self.keys[i] = None
        self.vals[i] = None
        # Rehash all keys in same cluster
        i = (i + 1) % self.m
        while self.keys[i] is not None:
            # Delete keys[i] and values[i] and reinsert
            keyToRehash = self.keys[i]
            valueToReash = self.values[i]
            self.keys[i] = None
            self.vals[i] = None
            self.n -= 1
            self.put(keyToRehash, valueToReash)
            i = (i + 1) % self.m
        self.n -= 1

        # Halves table size if it's less than 12.5% full
        if self.n > 0 and self.n <= self.m / 8:
            self._resize(self.m // 2)

    def _resize(self, capacity):
        temp = LinearProbingHashST(capacity)
        for i in range(self.m):
            if self.keys[i] is not None:
                temp.put(self.keys[i], self.vals[i])
        self.keys = temp.keys
        self.vals = temp.vals
        self.m = temp.m

    def __len__(self):
        return self.n

    def __str__(self):
        pass


if __name__ == '__main__':
    dictionary = LinearProbingHashST(M=10)
    for i in range(20):
        dictionary.put(i, f'test{i}')
    print(dictionary.get(19))
