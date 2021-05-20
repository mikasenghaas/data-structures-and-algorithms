# solution to wiener index in may 2018 dsa exam
from itu.algs4.graphs.graph import Graph
from itu.algs4.fundamentals.queue import Queue
from itertools import combinations

G = Graph(7)
G.add_edge(0, 1)
G.add_edge(0, 2)
G.add_edge(1, 3)
G.add_edge(1, 4)
G.add_edge(2, 5)
G.add_edge(2, 6)


def shortest_path(G, u, v):
    marked = [False] * G.V()
    edge_to = [None] * G.V()

    q = Queue()
    marked[u] = True
    q.enqueue(u)

    while not q.is_empty():
        s = q.dequeue()
        for adj in G.adj(s):
            if not marked[adj]:
                marked[s] = True
                edge_to[adj] = s
                q.enqueue(adj)

    dist = 0
    curr = v
    while edge_to[curr] != None:
        dist += 1
        curr = edge_to[curr]

    return dist


def wiener_index(G):
    # find all possible pairs
    pairs = list(combinations(list(range(G.V())), r=2))

    wiener_index = 0
    for u, v in pairs:
        wiener_index += shortest_path(G, u, v)

    return wiener_index

    # compute the sum of all shortest path


print(wiener_index(G))
