# python implementation to find cycles in a graph

from itu.algs4.graphs.graph import Graph
from itu.algs4.graphs.digraph import Digraph


class Cycles:
    def __init__(self, G, s=0):
        self._G = G
        self._marked = [False] * G.V()
        self._s = s
        self._has_cycle = False

        for s in range(G.V()):
            if not self._marked[s]:
                self.dfs(-1, s)

    def dfs(self, u, v):
        self._marked[v] = True
        for adj in self._G.adj(v):
            if not self._marked[adj]:
                self.dfs(v, adj)
            elif u != adj:
                self._has_cycle = True

    def has_cycle(self):
        return self._has_cycle


if __name__ == '__main__':
    G = Graph(7)
    G.add_edge(0, 1)
    G.add_edge(0, 2)
    G.add_edge(0, 5)
    G.add_edge(0, 6)
    G.add_edge(3, 4)
    G.add_edge(3, 5)
    G.add_edge(4, 5)
    G.add_edge(4, 6)
    G.add_edge(1, 3)
    print(G)

    cycle_detector = Cycles(G)
    print(cycle_detector.has_cycle())
