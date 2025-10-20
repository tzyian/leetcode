def bellman_ford(graph, start):
    dists = {node: float("inf") for node in graph}
    dists[start] = 0

    # Relax edges up to |V| - 1 times
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, w in graph[u]:
                if dists[u] + w < dists[v]:
                    dists[v] = dists[u] + w

    # Check for negative-weight cycles
    for u in graph:
        for v, w in graph[u]:
            if dists[u] + w < dists[v]:
                raise ValueError("Graph contains a negative-weight cycle")

    return dists
