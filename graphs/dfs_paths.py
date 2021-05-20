# depth first search in python (based on sedgewick and wayne, itu.algs4 library)

from itu.algs4.graphs.graph import Graph
from itu.algs4.graphs.digraph import Digraph
from itu.algs4.fundamentals.stack import Stack


class Paths:
    def __init__(self, G, s=0):
        self._G = G  # graph
        self._marked = [False] * G.V()  # keep track of visited nodes
        self._edgeto = [0] * G.V()
        self._count = 0  # number of reachable nodes from source s
        self._s = s  # source node (start dfs from there)

        # start dfs on intialisation
        self.dfs(G, s)

    def dfs(self, G, s):
        self._marked[s] = True
        self._count += 1

        for a in G.adj(s):
            if self._marked[a] == False:
                self._edgeto[a] = s
                self.dfs(G, a)

    def has_path_to(self, v: int):
        return self._marked[v]

    def path_to(self, v: int):
        if not self.has_path_to(v):
            return None
        path = Stack()
        curr = v
        while curr != self._s:
            path.push(curr)
            curr = self._edgeto[curr]
        path.push(self._s)
        return path

    def connected(self):
        return self._count == self._G.V()


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

    paths = Paths(G, s=0)
    print(paths._marked)
    print(paths._edgeto)
    print(f"Is Connected: {paths.connected()}")
    for i in range(G.V()):
        if i is not paths._s:
            print(
                f'{paths._s} has path to {i}: {paths.has_path_to(i)} [{paths.path_to(i)}]')
