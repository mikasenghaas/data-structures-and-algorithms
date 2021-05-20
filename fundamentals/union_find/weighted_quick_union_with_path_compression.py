class WeightedQuickUnionWithPathCompressionUF():
    """
    Time complexity:
      constructor: O(n)
      union:       amortized ~O(1)
      find:        amortized ~O(1)
    """

    def __init__(self, n):
        self.uf = list(range(n))
        self.sizes = [1] * n
        self.cc = len(self.uf)

    def __repr__(self):
        return f"'roots': {self.uf}, 'count': {self.cc}"

    def union(self, p, q):
        if p == q:
            return
        p_root = self._root(p)
        q_root = self._root(q)
        if p_root == q_root:
            return

        if self.sizes[p_root] < self.sizes[q_root]:
            self.uf[p_root] = q_root
            self.sizes[q_root] += self.sizes[p_root]
        else:
            self.uf[q_root] = p_root
            self.sizes[p_root] += self.sizes[q_root]

        self.cc -= 1

    def _root(self, p):
        root = self.uf[p]
        while not root == self.uf[root]:
            self.uf[root] = self.uf[self.uf[root]]
            root = self.uf[root]
        self.uf[p] = root
        return root

    def find(self, p):
        return self._root(p)

    def connected(self, p, q):
        return p == q or self.find(p) == self.find(q)

    def count(self):
        return self.cc


if __name__ == '__main__':
    uf = WeightedQuickUnionWithPathCompressionUF(10)
    for i in range(1, 5):
        uf.union(0, i)
    print(uf)
