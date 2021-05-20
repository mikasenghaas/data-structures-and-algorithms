# compute the diameter for an undirected, weighted graph
import math
from itu.algs4.graphs.edge_weighted_graph import EdgeWeightedGraph, Edge
from itu.algs4.sorting.index_min_pq import IndexMinPQ


def eccentricity(G, u):
    # initialise data structures
    dist_to = [math.inf] * G.V()
    q = IndexMinPQ(G.V())

    # start from source
    dist_to[u] = 0
    q.insert(u, 0.0)

    while q.is_empty() == False:
        v = q.del_min()
        for e in G.adj(v):
            # relax edge
            w = e.other(v)
            # relax condition if we can make the path shorter
            if dist_to[w] > dist_to[v] + e.weight():
                dist_to[w] = dist_to[v] + e.weight()
                if q.contains(w):
                    q.decrease_key(w, dist_to[w])
                else:
                    q.insert(w, dist_to[w])
    return max(dist_to)


def diameter(G):
    # find the maximum eccentricity
    return max([eccentricity(G, u) for u in range(G.V())])


G = EdgeWeightedGraph(5)
G.add_edge(Edge(0, 1, 3))
G.add_edge(Edge(0, 2, 2))
G.add_edge(Edge(1, 3, 1))
G.add_edge(Edge(2, 3, 3))
G.add_edge(Edge(2, 4, 2))
G.add_edge(Edge(3, 4, 2))
print(diameter(G))
