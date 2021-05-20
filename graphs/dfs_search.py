# depth first search in python (based on sedgewick and wayne, itu.algs4 library)

from itu.algs4.graphs.graph import Graph
from itu.algs4.graphs.digraph import Digraph


class Search:
    def __init__(self, G, s=0, visit_all=False):
        self._G = G  # graph
        self._marked = [False] * G.V()  # keep track of visited nodes
        self._id = [None] * G.V()
        self._count = 0  # number of reachable nodes from source s
        self._cc = 1  # count connected compartment
        self._s = s  # source node (start dfs from there)

        # start dfs on intialisation
        self.dfs(G, s)

        if visit_all == True:
            for i in range(self._G.V()):
                if self._marked[i] == False:
                    self._cc += 1
                    self.dfs(G, i)

    def dfs(self, G, s):
        print(f'visiting: {s}')
        self._marked[s] = True
        self._id[s] = self._cc
        self._count += 1

        for a in G.adj(s):
            if self._marked[a] == False:
                self.dfs(G, a)

    def has_path_to(self, v: int):
        return self._id[self._s] == self._id[v]

    def marked(self, v: int):
        return self._marked[v]

    def count(self):
        return self._count

    def connected(self):
        return self._cc == 1


# client code
if __name__ == '__main__':
    # initialise example graph
    G = Graph(7)
    G.add_edge(0, 1)
    G.add_edge(0, 2)
    G.add_edge(0, 5)
    G.add_edge(0, 6)
    G.add_edge(3, 4)
    G.add_edge(3, 5)
    G.add_edge(5, 4)
    G.add_edge(4, 6)
    print(G)

    searcher = Search(G, s=0)
    print(searcher._id)
    print(f"Is Connected: {searcher.connected()}")
    for i in range(G.V()):
        if i is not searcher:
            print(f'{searcher._s} has path to {i}: {searcher.has_path_to(i)}')
