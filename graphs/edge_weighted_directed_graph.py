from itu.algs4.fundamentals.bag import Bag


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


class EdgeWeightedDigraph:
    def __init__(self, V):
        self._V = V
        self._E = 0
        self._indegree = [0] * V
        self._adj = [None] * V
        for v in range(V):
            self._adj[v] = Bag()

    def V(self):
        return self._V

    def E(self):
        return self._E

    def add_edge(self, e):
        v = e.from_vertex()
        w = e.to_vertex()
        self._adj[v].add(e)
        self._indegree[w] += 1
        self._E += 1

    def adj(self, v):
        return self._adj[v]

    def outdegree(self, v):
        return self._adj[v].size()

    def indegree(self, v):
        return self._indegree[v]

    def edges(self):
        edges = Bag()
        for v in range(self._V):
            for e in self._adj[v]:
                edges.add(e)
        return edges

    def __repr__(self):
        s = ["{} {} \n".format(self._V, self._E)]
        for v in range(self._V):
            s.append("{}: ".format(v))
            for e in self._adj[v]:
                s.append("{}  ".format(e))
            s.append("\n")
        return "".join(s)
