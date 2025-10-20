def floyd_warshall(n: int, edges: list[tuple[int, int, int]]) -> list[list[int]]:
    inf = 10**9 + 7
    dists = [[inf] * n for _ in range(n)]

    for u, v, wt in edges:
        dists[u][v] = wt

    for i in range(n):
        dists[i][i] = 0

    # it's k first then i then j
    # because we want to consider all paths that go through k
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dists[i][j] = min(dists[i][j], dists[i][k] + dists[k][j])

    return dists
