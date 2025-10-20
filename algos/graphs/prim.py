from collections import defaultdict
from typing import List
from heapq import heappush, heappop


# Prim's algorithm to find the Minimum Spanning Tree (MST) of a connected, undirected graph.
# (V+E) log V
# VlogV for the heap operations
# ElogV for the edge relaxations

# edges: List of edges in the format [weight, node1, node2]


def prim(edges: List[List[int]]):
    n = len(edges)
    inf = 10**10
    graph = defaultdict(dict)

    for u, x, y in edges:
        graph[x][y] = u
        graph[y][x] = u

    visited = [False] * n  # alr in MST

    cheapest = [inf] * n  # cheapest edge to get from i to MST
    cheapest[0] = 0

    mst = []
    total_wt = 0

    # (weight, u, v)
    heap = [(0, 0, 0)]
    while heap and len(mst) < n - 1:
        w, u, v = heappop(heap)
        if visited[v]:
            continue

        total_wt += w
        visited[v] = True
        mst.append((w, u, v))

        for nb, nw in graph[v].items():
            if not visited[nb] and nw < cheapest[nb]:
                cheapest[nb] = nw
                heappush(heap, (nw, v, nb))

    return total_wt, mst
