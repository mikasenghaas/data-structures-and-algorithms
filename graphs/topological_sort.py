from itu.algs4.fundamentals.stack import Stack
from itu.algs4.fundamentals.queue import Queue
from itu.algs4.graphs.digraph import Digraph
from itu.algs4.graphs.symbol_digraph import SymbolDigraph


class DirectedCycle:
    def __init__(self, digraph):
        self._cycle = None
        self._on_stack = [False] * digraph.V()
        self._edge_to = [0] * digraph.V()
        self._marked = [False] * digraph.V()
        for v in range(digraph.V()):
            if not self._marked[v]:
                self._dfs(digraph, v)

    # check that algorithm computes either the topological order or finds a directed cycle
    def _dfs(self, digraph, v):
        self._on_stack[v] = True
        self._marked[v] = True
        for w in digraph.adj(v):
            # short circuit if directed cycle found
            if self.has_cycle():
                return
            # found new vertex, so recur
            elif not self._marked[w]:
                self._edge_to[w] = v
                self._dfs(digraph, w)
            # found a cycle if adj vertex on current recursive directed path
            elif self._on_stack[w]:
                self._cycle = Stack()  # data structure to trace back cycle
                # trace back starting from vertex before creating loop (v)
                x = v
                while x != w:  # iterate back until at vertex that creates cycle
                    self._cycle.push(x)
                    x = self._edge_to[x]
                # push cycle node on stack and initial node to complete cycle (at least two equal vertices)
                self._cycle.push(w)
                self._cycle.push(v)

        # remove current vertex from on stack if all neighbours if we move up one recursive level
        self._on_stack[v] = False

    def has_cycle(self):
        return self._cycle is not None

    def cycle(self):
        return self._cycle


class DepthFirstOrder:
    def __init__(self, G):
        self._G = G
        self._pre = Queue()
        self._post = Queue()
        self._reverse_post = Stack()

        self._marked = [False] * G.V()
        for v in range(G.V()):
            if not self._marked[v]:
                self.dfs(v)

    def dfs(self, v):
        self._pre.enqueue(v)
        self._marked[v] = True

        for w in self._G.adj(v):
            if not self._marked[w]:
                self.dfs(w)

        self._post.enqueue(v)
        self._reverse_post.push(v)

    def pre(self):
        return self._pre

    def post(self):
        return self._post

    def reverse_post(self):
        return self._reverse_post


class Topological:
    def __init__(self, digraph):
        self._order = None

        finder = DirectedCycle(digraph)

        if not finder.has_cycle():
            dfs = DepthFirstOrder(digraph)
            self._order = dfs.reverse_post()
            self._rank = [0] * digraph.V()
            i = 0
            for v in self._order:
                self._rank[v] = i
                i += 1

    def has_order(self):
        return self._order is not None

    def order(self):
        return self._order

    def rank(self, v):
        if self.has_order():
            return self._rank[v]
        else:
            return -1


if __name__ == '__main__':
    graph = Digraph(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(2, 3)
    graph.add_edge(4, 0)
    graph.add_edge(2, 4)

    # cycles = DirectedCycle(graph)
    topo = Topological(graph)
    print(topo.has_order())
    print(topo.order())
