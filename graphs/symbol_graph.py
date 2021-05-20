from itu.algs4.graphs.graph import Graph
from itu.algs4.searching.binary_search_st import BinarySearchST


class SymbolGraph:
    """The SymbolGraph class represents an undirected graph, where the vertex
    names are arbitrary strings. By providing mappings between vertex names and
    integers, it serves as a wrapper around the Graph data type, which assumes
    the vertex names are integers between 0 and V - 1.
    """

    def __init__(self, vertices):
        self._st = BinarySearchST()  # string -> index

        # built symbol table to translate strings into indices
        for i in range(len(vertices)):
            self._st.put(vertices[i], i)

        # built array to translate from indices to strings
        self._keys = [None] * self._st.size()  # index  -> string
        for name in self._st.keys():
            self._keys[self._st.get(name)] = name

        # initialise graph
        self._graph = Graph(self._st.size())  # the underlying graph

    def V(self):
        return self._graph._V

    def E(self):
        return self._graph._E

    def size(self):
        return self._graph._V

    def __len__(self):
        return self._graph._V

    def contains(self, s):
        return self._st.contains(s)

    def index_of(self, s):
        return self._st.get(s)

    def name_of(self, v):
        return self._keys[v]

    def add_edge(self, u, v):
        self._graph.add_edge(self.index_of(u), self.index_of(v))

    def adj(self, u):
        return [self.name_of(adj) for adj in self._graph.adj(self.index_of(u))]

    def degree(self, u):
        return self._graph.degree(self.index_of(u))

    def graph(self):
        return self._graph


if __name__ == '__main__':
    graph = SymbolGraph(['mika', 'louis', 'emma', 'sofie', 'iben'])

    graph.add_edge('mika', 'louis')
    graph.add_edge('emma', 'louis')
    print(graph._graph)
    print(graph.contains('mika'))
    print(graph.adj('mika'))
