# python implementation of quick find

class QuickUnionUF:
    def __init__(self, n):
        # compartments named through integers 0 to n-1
        self.uf = [i for i in range(n)]
        self.n = n
        self.cc = n

    def size(self):
        return self.n

    def count(self):
        return self.cc

    def find(self, p):
        while p != self.uf[p]:
            p = self.uf[p]
        return p

    def connected(self, p, q):
        # O(sum of height of both compartment trees)
        return self.find(p) == self.find(q)

    def union(self, p, q):
        # O(log(n))
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return

        self.uf[root_q] = root_p  # point tree of p to root of tree of q
        self.cc -= 1  # decrement number of connected components

    def __len__(self):
        return self.n

    def __str__(self):
        string = '[ '
        for i in range(self.n):
            string += f'{self.uf[i]} '
        return string + ']'


if __name__ == '__main__':
    uf = QuickUnionUF(10)
    for i in range(1, 5):
        uf.union(0, i)
    print(uf.connected(1, 2))
    print(uf.count())
