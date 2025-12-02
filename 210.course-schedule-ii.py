# @leet imports start
from collections import defaultdict
from typing import *

# @leet imports end


# @leet start
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


# @leet end

