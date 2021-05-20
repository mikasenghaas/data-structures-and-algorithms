# python implementation of quick find

class QuickFindUF:
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
        return self.uf[p]

    def connected(self, p, q):
        # O(1)
        return self.find(p) == self.find(q)

    def union(self, p, q):
        # O(n)
        if self.find(p) == self.find(q):
            return

        p_id = self.find(p)
        q_id = self.find(q)

        for i in range(self.n):
            if self.uf[i] == p_id:
                self.uf[i] = q_id
        self.cc -= 1

    def __len__(self):
        return self.n

    def __str__(self):
        string = '[ '
        for i in range(self.n):
            string += f'{self.uf[i]} '
        return string + ']'


if __name__ == '__main__':
    uf = QuickFindUF(5)
    uf.union(2, 3)
    print(uf)
    uf.union(2, 4)
    print(uf)
