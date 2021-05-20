# python implementation of an edge-weighted graph
from itu.algs4.fundamentals.bag import Bag


class Edge:
    def __init__(self, v, w, weight):
        self._v = v
        self._w = w
        self._weight = weight

    def v(self):
        return self._v

    def w(self):
        return self._w

    def weight(self):
        return self._weight

    def either(self):
        return self._v

    def other(self, u):
        if u == self._v:
            return self._w
        elif u == self._w:
            return self._v
        else:
            raise ValueError('Invalid Argument')

    def __lt__(self, other):
        if self._weight < other._weight:
            return True
        else:
            return False

    def __str__(self):
        return f'{self._v}-{self._w}: {self._weight}'


class UndirectedEdgeWeightedGraph:
    def __init__(self, V):
        self._V = V
        self._E = 0

        self._adj = [Bag() for _ in range(V)]

    def V(self):
        return self._V

    def E(self):
        return self._E

    def adj(self, v):
        return self._adj[v]

    def add_edge(self, v, w, weight=1):
        self._adj[v].add(Edge(v, w, weight))
        self._adj[w].add(Edge(w, v, weight))
        self._E += 1

    def __str__(self):
        string = f'{self.V()} vertices, {self.E()} edges\n'
        for i in range(self.V()):
            string += f'{i}: {self._adj[i]}\n'
        return string


if __name__ == '__main__':
    G = UndirectedEdgeWeightedGraph(4)
    G.add_edge(0, 1, 10)
    G.add_edge(1, 2, 2)
    G.add_edge(2, 3, 3)
    G.add_edge(3, 1, 5)

    print(G)
