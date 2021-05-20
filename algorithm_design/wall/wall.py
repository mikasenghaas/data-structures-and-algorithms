# solving building wall from dsa 2017 exam
import sys
from itu.algs4.sorting.index_min_pq import IndexMinPQ
from itu.algs4.fundamentals.queue import Queue
import math

world = [line.strip().split() for line in sys.stdin.readlines()]
R = len(world)  # no of rows
# maximum number of columns (length)
L = max([len(world[i]) for i in range(R)])
# print(world)


def adjacents(R, L, i, j):
    # function to return a list of adjacents indices
    if i < 0 or i > R-1 or j < 0 or j > L-1:
        return
    adjacents = []
    if i-1 >= 0:
        adjacents.append((i-1, j))  # top
    if i+1 <= R-1:
        adjacents.append((i+1, j))  # bottom
    if j-1 >= 0:
        adjacents.append((i, j-1))  # left
    if j+1 <= L-1:
        adjacents.append((i, j+1))  # right

    return adjacents


def solve(world, R, L):
    # find starting indices
    start_from = []
    for j in range(R):
        if world[j][0] == 'P':
            start_from.append((j, 1))

    # dijkstra shortest path finding from starting positions to the right
    min_distances = []
    for index in start_from:
        i, j = index
        # built dist_to array
        dist_to = []
        for _ in range(R):
            line = []
            for _ in range(L):
                line.append(math.inf)
            dist_to.append(line)

        # intialise starting position
        dist_to[i][j] = int(world[i][j])
        q = Queue()
        q.enqueue((i, j))

        while not q.is_empty():
            v = q.dequeue()  # dequeue current index
            for adj in adjacents(R, L, v[0], v[1]):
                i, j = adj[0], adj[1]
                if world[i][j] in ['P', 'U', 'M', 'A', '.']:
                    # print(f'found: {world[i][j]}')
                    continue
                else:
                    # if distance can be decreased, decrease
                    if dist_to[i][j] > int(world[i][j]) + dist_to[v[0]][v[1]]:
                        dist_to[i][j] = int(world[i][j]) + dist_to[v[0]][v[1]]
                        q.enqueue(adj)
        min_distances.append(min([dist_to[i][L-2] for i in range(R)]))

    return min(min_distances)


print(solve(world, R, L))
