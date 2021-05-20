# python implementation of a trie
R = 256


class Node:
    def __init__(self):
        self.val = None
        self.next = [None] * R


class Trie:
    def __init__(self):
        self.root = Node()
        self.n = 0

    def size(self):
        return self.n

    def __len__(self):
        return self.size()

    def contains(self, key):
        return self.get(key) != None

    def put(self, key, val):
        self.root = self._put(self.root, key, val, 0)

    def _put(self, curr, key, val, d):
        if curr is None:
            curr = Node()
        if d == len(key):
            if curr.val is None:
                self.n += 1
            curr.val = val
            return curr
        c = key[d]
        curr.next[ord(c)] = self._put(curr.next[ord(c)], key, val, d + 1)
        return curr

    def get(self, key):
        # start recursive search in trie
        x = self._get(self.root, key, 0)

        return None if x is None else x.val

    def _get(self, curr, key, d):
        if curr is None:  # search miss
            return None
        if d == len(key):  # search hit
            return curr
        # search further recursively
        c = key[d]
        return self._get(curr.next[ord(c)], key, d + 1)


if __name__ == '__main__':
    ST = Trie()
    ST.put('name', 'mika')
    ST.put('age', 19)
    ST.put('location', 'copenhagen')
    ST.put('age', 20)

    print(ST.get('name'))
    print(ST.get('age'))
    print(ST.contains('age'))
    print(ST.size())
