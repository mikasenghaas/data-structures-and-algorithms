# python implementation to test for bipartiteness in a given undirected graph
from itu.algs4.graphs.graph import Graph

# only works for simple graphs (no self-loops)


class Bipartite:
    def __init__(self, G, s=0):
        self._G = G
        self._marked = [False] * G.V()
        self._coloring = [False] * G.V()
        self._is_bipartite = True

        for s in range(G.V()):
            if not self._marked[s]:
                self.dfs(s)

    def dfs(self, s):
        self._marked[s] = True

        for adj in self._G.adj(s):
            if not self._marked[adj]:
                self._coloring[adj] = not self._coloring[s]
                self.dfs(adj)
            elif self._coloring[s] == self._coloring[adj]:
                self._is_bipartite = False

    def is_bipartite(self):
        return self._is_bipartite

    def coloring(self):
        if not self.is_bipartite():
            raise ValueError('No two-coloring possible')
        return ['Red' if self._coloring[i]
                else 'Blue' for i in range(len(self._coloring))]


if __name__ == '__main__':
    G = Graph(4)
    G.add_edge(0, 1)
    G.add_edge(0, 2)
    G.add_edge(0, 3)
    print(G)

    colorer = Bipartite(G)
    print(colorer.coloring())
    print(colorer.is_bipartite())
