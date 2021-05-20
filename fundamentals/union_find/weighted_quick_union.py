# python implementation of weighted quick-union find

class WeightedQuickUnionUF:
    def __init__(self, n):
        # compartments named through integers 0 to n-1
        self.uf = [i for i in range(n)]
        self.size = [1] * n
        self.n = n
        self.cc = n

    def number_of_singletons(self):
        return self.n

    def tree_size(self, p):
        return self.size[self.find(p)]

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

        # make root of smaller rank point to root of larger rank
        if self.size[root_p] < self.size[root_q]:
            small, large = root_p, root_q
        else:
            small, large = root_q, root_p

        self.uf[small] = large
        self.size[large] += self.size[small]

        self.cc -= 1  # decrement number of connected components

    def move(self, p, q):
        # move node p into set of q
        root = self.find(p)
        children = [site for site in range(
            self.n) if self.uf[site] == p and site != p]

        # rearranging forest of p
        if root == p:  # first case: moving node is root
            for child in children:
                # arbitrary reconnect to first child
                self.uf[child] = children[0]
        else:
            for child in children:
                # reconnect children of p to root
                self.uf[child] = root

        # moving p to point to root of q
        self.uf[p] = self.find(q)

    def __len__(self):
        return self.n

    def __str__(self):
        string = '[ '
        for i in range(self.n):
            string += f'{self.uf[i]} '
        return string + ']'


if __name__ == '__main__':
    uf = WeightedQuickUnionUF(10)
    for i in range(1, 5):
        print(uf)
        uf.union(0, i)
        print(uf)
        print('\n')
    print(uf)
