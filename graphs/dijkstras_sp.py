# python implementation of dijkstra's algorithm to solve the single-source shortest path
from itu.algs4.fundamentals.stack import Stack
from itu.algs4.graphs.edge_weighted_digraph import EdgeWeightedDigraph
from itu.algs4.sorting.index_min_pq import IndexMinPQ
import math


class DirectedEdge:
    def __init__(self, u, v, weight=1):
        self._u = u
        self._v = v
        self._weight = weight

    def from_vertex(self):
        return self._u

    def to_vertex(self):
        return self._v

    def weight(self):
        return self._weight

    def __lt__(self, other):
        if self.weight() < other.weight():
            return True
        return False

    def __repr__(self):
        return f"{self._u}->{self._v} {float(self._weight)}"


class DijkstraSP:
    def __init__(self, G, s=0):
        for e in G.edges():
            if e.weight() < 0:
                raise ValueError("edge {} has negative weight".format(e))
        self._dist_to = [math.inf] * G.V()
        self._edge_to = [None] * G.V()

        # initialise source distance to 0 by convention
        self._dist_to[s] = 0.0

        # initialising index min pq to keep track of vertices that are candidates for being relaxed next
        self._pq = IndexMinPQ(G.V())
        self._pq.insert(s, 0.0)

        # iterate until all vertices possibly reachable are reached
        while not self._pq.is_empty():
            v = self._pq.del_min()
            for e in G.adj(v):
                self._relax(e)

    def dist_to(self, v):
        return self._dist_to[v]

    def has_path_to(self, v):
        return self._dist_to[v] < float("inf")

    def path_to(self, v):
        if not self.has_path_to(v):
            return None
        path = Stack()
        e = self._edge_to[v]
        while e is not None:
            path.push(e)
            e = self._edge_to[e.from_vertex()]
        return path

    def _relax(self, e):
        v = e.from_vertex()
        w = e.to_vertex()
        if self._dist_to[w] > self._dist_to[v] + e.weight():
            self._dist_to[w] = self._dist_to[v] + e.weight()
            self._edge_to[w] = e
            if self._pq.contains(w):
                self._pq.decrease_key(w, self._dist_to[w])
            else:
                self._pq.insert(w, self._dist_to[w])


if __name__ == '__main__':
    G = EdgeWeightedDigraph(5)
    G.add_edge(DirectedEdge(0, 1, 2))
    G.add_edge(DirectedEdge(0, 2, 2))
    G.add_edge(DirectedEdge(0, 3, 4))
    G.add_edge(DirectedEdge(2, 3, 1))
    G.add_edge(DirectedEdge(1, 4, 3))
    G.add_edge(DirectedEdge(3, 4, 6))

    spt = DijkstraSP(G)
    for i in range(5):
        print(spt.path_to(i), spt.dist_to(i))
