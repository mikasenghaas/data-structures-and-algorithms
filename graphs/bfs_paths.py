# breadth first paths in python (based on sedgewick and wayne, itu.algs4 library)

from itu.algs4.graphs.graph import Graph
from itu.algs4.graphs.digraph import Digraph
from itu.algs4.fundamentals.queue import Queue
from itu.algs4.fundamentals.stack import Stack


class Paths:
    def __init__(self, G, s=0):
        self._G = G  # graph
        self._marked = [False] * G.V()  # keep track of visited nodes
        # parent-link representation of shortest path tree
        self._edgeto = [None] * G.V()
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
                    self._edgeto[adj] = s
                    self._count += 1
                    q.enqueue(adj)

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
    G.add_edge(4, 5)
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
