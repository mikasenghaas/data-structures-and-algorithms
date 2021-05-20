# breadth first search in python (based on sedgewick and wayne, itu.algs4 library)

from itu.algs4.graphs.graph import Graph
from itu.algs4.graphs.digraph import Digraph
from itu.algs4.fundamentals.queue import Queue


class Search:
    def __init__(self, G, s=0):
        self._G = G  # graph
        self._marked = [False] * G.V()  # keep track of visited nodes
        self._count = 0  # number of reachable nodes from source s
        self._s = s  # source node (start dfs from there)

        # start dfs on intialisation
        self.bfs(G, s)

    def bfs(self, G, s):
        # mark source node and insert into queue to initialise bfs
        self._marked[s] = True
        q = Queue()
        q.enqueue(s)

        # continue bfs until queue is empty (all reachable nodes have been visited)
        while q.is_empty() == False:
            s = q.dequeue()
            for adj in G.adj(s):
                if self._marked[adj] == False:
                    self._marked[adj] = True
                    q.enqueue(adj)
                    self._count += 1

    def has_path_to(self, v: int):
        return self._marked[v]

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

    searcher = Search(G, s=0)
    print(f"Is Connected: {searcher.connected()}")
    print(searcher._count)
    for i in range(G.V()):
        if i is not searcher:
            print(f'{searcher._s} has path to {i}: {searcher.has_path_to(i)}')
