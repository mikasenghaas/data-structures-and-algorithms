# DSA 2021 Exam, Question 4: Algorithmic Design
# Author: Jonas-Mika Senghaas (jsen@itu.dk)

import sys
import math
from itu.algs4.graphs.edge_weighted_digraph import EdgeWeightedDigraph
from itu.algs4.graphs.directed_edge import DirectedEdge
from itu.algs4.sorting.index_min_pq import IndexMinPQ

# read input
h = int(sys.stdin.readline())
weights = [[int(i) for i in line.strip().split()]
           for line in sys.stdin.readlines()]

# print(h)
# print(weights)


def solve(h, weights):
    # construct complete binary tree
    weights = [item for sublist in weights for item in sublist]
    h += 1
    V = int((h * (h+1)) / 2)
    G = EdgeWeightedDigraph(V)

    # construct edges of the graph
    _sum = 0
    added_edges = 0
    for level in range(0, h):
        for i in range(level):
            #print(f'add: {_sum+i}, {_sum+i+level}')
            G.add_edge(DirectedEdge(_sum + i, _sum +
                                    i + level, weights[added_edges]))
            added_edges += 1
            #print(f'add: {_sum+i}, {_sum+i+level+1}')
            G.add_edge(DirectedEdge(_sum + i, _sum + i +
                                    level + 1, weights[added_edges]))
            added_edges += 1
        _sum += level

    dist_to = [math.inf for _ in range(V)]

    q = IndexMinPQ(G.V())
    q.insert(0, 0.0)  # enqueue root
    dist_to[0] = 0.0

    # iterate until all vertices possibly reachable are reached
    while not q.is_empty():
        u = q.del_min()
        for e in G.adj(u):
            u = e.from_vertex()
            v = e.to_vertex()
            if dist_to[v] > dist_to[u] + e.weight():
                dist_to[v] = dist_to[u] + e.weight()
                if q.contains(v):
                    q.decrease_key(v, dist_to[v])
                else:
                    q.insert(v, dist_to[v])

    # while not q.is_empty():
    #    curr = q.dequeue()
    #    for adj in G.adj(curr):
    #        u = curr
    #        v = adj.other(u)
    #        if dist_to[v] > dist_to[u] + adj.weight():
    #            dist_to[v] = dist_to[u] + adj.weight()
    #            q.enqueue(v)

    # get minimum of leaves
    return int(min(dist_to[len(dist_to)-h:]))


print(solve(h, weights))
