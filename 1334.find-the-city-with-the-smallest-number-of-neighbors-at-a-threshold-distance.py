from typing import List

# This is Bellman-Ford


# @leet start
class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        inf = 10**10

        dists = [[inf] * n for _ in range(n)]

        for u, v, wt in edges:
            dists[u][v] = wt
            dists[v][u] = wt

        for i in range(n):
            dists[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dists[i][j] = min(dists[i][j], dists[i][k] + dists[k][j])

        best_city = -1
        mins = inf
        for i in range(n):
            cities = len([j for j in dists[i] if j <= distanceThreshold])
            if cities <= mins:
                mins = cities
                best_city = i

        return best_city


# @leet end

n = 4
e = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
d = 4
x = Solution().findTheCity(n, e, d)
print(x)

5
[[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]]
2
