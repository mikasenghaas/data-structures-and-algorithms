# finding diameter in undirected, unweighted, connected graph using bfs
from itu.algs4.graphs.graph import Graph
from itu.algs4.fundamentals.queue import Queue

# O(V + E)


def diameter(G):
    marked = [False] * G.V()
    edge_to = [None] * G.V()
    q = Queue()

    marked[0] = True
    q.enqueue(0)

    while not q.is_empty():
        v = q.dequeue()
        for adj in G.adj(v):
            if marked[adj] == False:
                marked[adj] = True
                edge_to[adj] = v
                q.enqueue(adj)

    # compute dist of all paths
    paths = []
    for i in range(G.V()):
        dist = 0
        curr = i
        while edge_to[curr] != None:
            dist += 1
            curr = edge_to[curr]

        paths.append(dist)

    return max(paths)


G = Graph(7)
G.add_edge(0, 1)
G.add_edge(0, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(2, 4)
G.add_edge(3, 4)
G.add_edge(5, 4)
G.add_edge(5, 6)
G.add_edge(3, 6)

print(diameter(G))
