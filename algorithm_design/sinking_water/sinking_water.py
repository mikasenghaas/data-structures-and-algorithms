# algorithmic solution question 4 in aug 2019 dsa exam
from itu.algs4.fundamentals.bag import Bag
from itu.algs4.fundamentals.queue import Queue


class AdjacencyListGraph():
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
        return "".join(s)


world = [[0, 2, -1, 0],
         [1, 0, 2, -1],
         [0, 0, 0, -1]]


class Graph:
    def __init__(self):
        pass


def connected_inhabitants(L):
    # initialise number of days
    d = 0

    # find source
    i = 0
    for x in L:
        if x == 0:
            break
        i += 1

    while True:
        print(L)

        # total number of grass fields
        total_count = len([x for x in L if x == 0])

        count = 1
        l, r = i-1, i+1
        while l >= 0 and L[l] == 0:
            count += 1
            l -= 1
        while r < len(L) and L[r] == 0:
            count += 1
            r += 1

        if count == total_count:
            return d

        if len([x for x in L if x > 0]) == 0:  # base case (no more lowering of water possible)
            return 'impossible'

        d += 1
        for j in range(len(L)):
            if L[j] > 0:
                L[j] -= 1


def connected_inhabitans_multiworld(L):
    # intialise graph object with V vertices
    R = len(L[0])
    C = len(L)

    flat_L = [item for sublist in L for item in sublist]
    V = len(flat_L)
    G = AdjacencyListGraph(V)

    # add horizontal edges
    for i in range(R-1):
        for j in range(C):
            G.add_edge(i+(R*j), i+(R*j)+1)
    # add right diagonal edges
    for i in range(R):
        for j in range(C-1):
            if j % 2 == 0:
                G.add_edge(i+(R*j), i+(R*j) + R)
            else:
                if i >= R-1:
                    break
                G.add_edge(i+(R*j), i+(R*j) + R+1)

    # add left diagonal edges
    for i in range(R):
        for j in range(C-1):
            if j % 2 == 0:
                if i == 0:
                    continue
                G.add_edge(i+(R*j), i+(R*j) + R-1)
            else:
                G.add_edge(i+(R*j), i+(R*j) + R)

    print(G)
    # create mapping
    mapping = {i: flat_L[i] for i in range(len(flat_L))}
    print(mapping)

    # find source
    s = 0
    for x in flat_L:
        if x == 0:
            break
        s += 1

    d = 0
    while True:
        print(d, mapping)
        # total number of grass fields
        total_count = len([x for x in mapping.values() if x == 0])

        marked = [False] * G.V()
        q = Queue()
        count = 1
        marked[s] = True
        q.enqueue(s)

        while q.is_empty() == False:
            v = q.dequeue()
            for adj in G.adj(v):
                if marked[adj] == False and mapping[adj] == 0:
                    marked[adj] = True
                    q.enqueue(adj)
                    count += 1

        print(total_count, count)

        if count == total_count:
            return d

        # base case (no more lowering of water possible)
        if len([x for x in mapping.values() if x > 0]) == 0:
            return 'impossible'

        d += 1
        for i in range(len(mapping)):
            if mapping[i] > 0:
                mapping[i] -= 1


print(connected_inhabitans_multiworld(world))
