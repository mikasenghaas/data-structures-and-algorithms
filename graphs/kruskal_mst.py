# python implementation of kruskal's algorithm
from itu.algs4.fundamentals.queue import Queue
from itu.algs4.sorting.min_pq import MinPQ
from itu.algs4.fundamentals.uf import WeightedQuickUnionUF

from itu.algs4.graphs.edge_weighted_graph import EdgeWeightedGraph
from itu.algs4.graphs.edge import Edge


class KruskalMST:
    def __init__(self, G):
        # initialise
        self._mst = Queue()
        self._edges = MinPQ()
        for edge in G.edges():
            self._edges.insert(edge)
        self._uf = WeightedQuickUnionUF(G.V())

        while not self._edges.is_empty() and self._mst.size() < G.V() - 1:
            min_edge = self._edges.del_min()
            u = min_edge.either()
            v = min_edge.other(u)
            if self._uf.connected(u, v):
                continue  # ineligible edge
            self._uf.union(u, v)  # union (are part of mst now)
            self._mst.enqueue(min_edge)

    def edges(self):
        return self._mst

    def weight(self):
        return sum([edge.weight() for edge in self._mst])


if __name__ == '__main__':
    G = EdgeWeightedGraph(4)
    G.add_edge(Edge(0, 1, 10))
    G.add_edge(Edge(1, 2, 2))
    G.add_edge(Edge(1, 3, 5))
    G.add_edge(Edge(2, 3, 3))

    mst = KruskalMST(G)
    print(mst.edges())
    print(mst.weight())
