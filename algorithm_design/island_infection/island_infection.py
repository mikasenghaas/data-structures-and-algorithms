# solution to island infection
import sys
from itu.algs4.fundamentals.bag import Bag
from itu.algs4.fundamentals.queue import Queue

R, C = [int(i) for i in sys.stdin.readline().split()]
world = [[int(i) for i in line.strip()] for line in sys.stdin.readlines()]


class Graph():
    """
    Undirected Graph, No Edge Weights, Allows Self-Loops and Parallel Edges
    """
    # construct empty graph

    def __init__(self, V):
        if V < 0:
            raise ValueError("Number of vertices must be nonnegative")
        self._V = V
        self._E = 0
        self._adj = []  # adjacency lists

        for _ in range(V):
            self._adj.append(Bag())  # Initialize all lists to empty bags.

    def V(self):
        return self._V

    def E(self):
        return self._E

    def size(self):
        return self._V

    def __len__(self):
        return self.size()

    def add_edge(self, v: int, w: int):
        self._adj[v].add(w)
        self._adj[w].add(v)
        self._E += 1

    def adj(self, v: int):
        return self._adj[v]

    def degree(self, v: int):
        return len(self.adj(v))

    def max_degree(self):
        _max = 0

        for v in range(self._V):
            if _max < len(self._adj[v]):
                _max = len(self._adj[v])
        return _max

    def average_degree(self):
        return 2 * (self._E / self._V)

    def number_self_loops(self):
        count = 0
        for v in range(self._V):
            for w in self._adj[v]:
                if v == w:
                    count += 1
        return int(count/2)

    def __repr__(self):
        s = [f"{self._V} vertices, {self._E} edges\n"]
        for v in range(self._V):
            s.append(f"{v} : ")
            for w in self._adj[v]:
                s.append(f" {w} ")
            s.append("\n")
        return ''.join(s)


def solve(R, C, world):
    flat_world = [item for sublist in world for item in sublist]
    G = Graph(len(flat_world))

    # add horizontal edges
    for i in range(R):
        for j in range(C-1):
            G.add_edge(j+(i*C), j+(i*C)+1)
    # add vertical edges
    for i in range(R-1):
        for j in range(C):
            G.add_edge(j+(i*C), j+(i*C)+C)

    # create mapping
    mapping = {i: flat_world[i] for i in range(len(flat_world))}
    # print(G)
    # print(mapping)

    # find virus and make it source
    s = 0
    for x in flat_world:
        if x == 2:
            break
        s += 1

    # start bfs from infection
    q = Queue()
    q.enqueue(s)

    while q.is_empty() == False:
        v = q.dequeue()
        for adj in G.adj(v):
            if mapping[adj] == 1:  # land
                mapping[adj] = 2  # infect the land
                q.enqueue(adj)
            elif mapping[adj] == 3:  # encounter human
                return 1
    return 0


print(solve(R, C, world))
