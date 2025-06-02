from heapq import heappop, heappush


# use a adjacency matrix to represent the graph
def dijkstra(graph: list[list[int]], start: int) -> tuple[list[int], list[int]]:

    n = len(graph)
    dists = [float('inf')] * n
    dists[start] = 0
    prev = {i: -1 for i in range(n)}
    pq = [(0, start)]  # (distance, node)

    while pq:
        d, u = heappop(pq)

        if d > dists[u]:
            continue

        for v in range(n):
            if graph[u][v] > 0:  # there is an edge
                distance = d + graph[u][v]
                if distance < dists[v]:
                    dists[v] = distance
                    prev[v] = u
                    heappush(pq, (distance, v))

    return dists, prev
