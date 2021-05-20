# directed graph api in python implemented using adjacency lists  (based on sedgewick and wayne, algs4 and itu.algs4 library)
from itu.algs4.fundamentals.bag import Bag


class AdjacencyListDiGraph():
    """
    Directed Graph, No Edge Weights, Allows Self-Loops and Parallel Edges
    """

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
        self._E += 1

    def adj(self, v: int):
        return self._adj[v]

    def out_degree(self, v: int):
        return len(self.adj(v))

    def in_degree(self, v: int):
        num = 0
        for i in range(self._V):
            for elm in self._adj[i]:
                if v == elm:
                    num += 1
        return num

    def max_degree(self):
        _max = 0

        for v in range(self._V):
            if _max < len(self._adj[v]):
                _max = len(self._adj[v])
        return _max

    def average_degree(self):
        return self._E / self._V

    def number_self_loops(self):
        count = 0
        for v in range(self._V):
            for w in self._adj[v]:
                if v == w:
                    count += 1
        return int(count/2)

    def reverse(self):
        copy = AdjacencyListDiGraph(self.V())
        for v in range(self.V()):
            for w in self.adj(v):
                copy.add_edge(w, v)
        return copy

    def __repr__(self):
        s = [f"{self._V} vertices, {self._E} edges\n"]
        for v in range(self._V):
            s.append(f"{v} : ")
            for w in self._adj[v]:
                s.append(f" {w} ")
            s.append("\n")

        return "".join(s)


class AdjacencyMatrixDiGraph:
    def __init__(self, V):
        self._V = V
        self._E = 0
        self.matrix = [[0 for _ in range(self._V)] for _ in range(self._V)]

    def V(self):
        return self._V

    def E(self):
        return self.E

    def size(self):
        return self.V()

    def add_edge(self, u, v):
        if u > self._V or v > self._V:
            raise ValueError('Vertex doesnt exist')
        self.matrix[u][v] = 1
        self._E += 1

    def adj(self, u):
        # O(V)
        return [i for i in range(self._V) if self.matrix[u][i] == 1]

    def out_degree(self, u):
        return sum(self.matrix[u])

    def in_degree(self, u):
        return sum([self.matrix[i][u] for i in range(self._V)])

    def average_degree(self):
        return self._E / self._V

    def number_self_loops(self):
        num = 0
        for i in range(self._V):
            if self.matrix[i][i] == 1:
                num += 1
        return num

    def reverse(self):
        copy = AdjacencyMatrixDiGraph(self.V())
        for v in range(self.V()):
            for w in self.adj(v):
                copy.add_edge(w, v)
        return copy

    def __str__(self):
        string = f'{self._V} vertices, {self._E} edges\n[' + str(
            self.matrix[0]) + '\n'
        for i in range(1, self._V-1):
            string += f' {self.matrix[i]}\n'
        return string + f' {self.matrix[-1]}]'


if __name__ == '__main__':
    graph = AdjacencyListDiGraph(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(2, 3)
    graph.add_edge(4, 0)
    graph.add_edge(2, 4)
    graph = graph.reverse()
    print(graph)
