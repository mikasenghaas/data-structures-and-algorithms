from itu.algs4.fundamentals.queue import Queue
from itu.algs4.sorting.min_pq import MinPQ
from itu.algs4.graphs.edge import Edge
from itu.algs4.graphs.edge_weighted_graph import EdgeWeightedGraph


class LazyPrimMST:
    def __init__(self, G):
        self._weight = 0.0  # total weight of MST
        self._mst = Queue()  # edges in the MST
        self._marked = [False] * G.V()  # marked[v] = True if v on tree
        self._pq = MinPQ()  # edges with one endpoint in tree

        for v in range(G.V()):  # run Prim from all vertices to
            if not self._marked[v]:
                self._prim(G, v)  # get a minimum spanning forest

    def _prim(self, G, s):
        # run prim's algorithm
        self._scan(G, s)
        while not self._pq.is_empty():  # better to stop when mst has V-1 edges
            e = self._pq.del_min()  # smallest edge on pq (frontier)
            v = e.either()  # two endpoints
            w = e.other(v)
            assert self._marked[v] or self._marked[w]
            if (
                self._marked[v] and self._marked[w]
            ):  # lazy, both v and w already scanned
                continue
            self._mst.enqueue(e)  # add e to MST
            self._weight += e.weight()
            if not self._marked[v]:
                self._scan(G, v)  # v becomes part of tree
            if not self._marked[w]:
                self._scan(G, w)  # w becomes part of tree

    def _scan(self, G, v):
        # add all edges e incident to v onto pq if the other endpoint has not yet been scanned
        assert not self._marked[v]
        self._marked[v] = True
        for e in G.adj(v):
            if not self._marked[e.other(v)]:
                self._pq.insert(e)

    def edges(self):
        return self._mst

    def weight(self):
        return self._weight


class EagerPrimMST:
    pass


if __name__ == '__main__':
    G = EdgeWeightedGraph(4)
    G.add_edge(Edge(0, 1, 10))
    G.add_edge(Edge(1, 2, 2))
    G.add_edge(Edge(1, 3, 5))
    G.add_edge(Edge(2, 3, 20))

    mst = LazyPrimMST(G)
    print(mst.edges())
    print(mst.weight())
