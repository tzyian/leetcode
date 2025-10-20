from collections import defaultdict
from typing import List


def topo_sort_dfs(n, edges):
    # build adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    visited = [0] * n  # 0=unvisited, 1=visiting, 2=done
    order = []

    def dfs(u):
        visited[u] = 1
        for v in graph[u]:
            if visited[v] == 0:
                dfs(v)
        visited[u] = 2
        order.append(u)

    for u in range(n):
        if visited[u] == 0:
            dfs(u)

    return order[::-1]  # reverse postorder


# Example
n = 6
edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
print(topo_sort_dfs(n, edges))
# Output: [5, 4, 2, 3, 1, 0]


class Solution:
    # TODO: the iterative version of this

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            # b is a prereq for a
            graph[b].append(a)

        visited = set()
        path = set()
        ans = []
        cycle = False

        def dfs(curr: int):
            nonlocal cycle
            if cycle:
                return

            visited.add(curr)
            path.add(curr)
            for nb in graph[curr]:
                if nb in path:
                    cycle = True
                    return
                if nb in visited:
                    continue
                dfs(nb)

            ans.append(curr)
            path.remove(curr)

        for c in range(numCourses):
            if c in visited:
                continue
            dfs(c)
            if cycle:
                return []

        return list(reversed(ans))
