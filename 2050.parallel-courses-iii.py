# @leet imports start
from functools import cache
from typing import List, Optional

# @leet imports end

from collections import defaultdict


# @leet start
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)

        # it's 1-indexed...
        for p, c in relations:
            p -= 1
            c -= 1
            graph[p].append(c)

        # toposort
        @cache
        def dfs(i: int) -> int:
            # no prereqs
            if not graph[i]:
                return time[i]

            # since we postorder dfs, we take the max of the timings
            # which is the max time to finish all its postreqs + current node
            ans = 0
            for nb in graph[i]:
                ans = max(ans, dfs(nb))
            return time[i] + ans

        ans = 0
        for i in range(n):
            ans = max(ans, dfs(i))

        return ans


# @leet end

n = 3
r = [[1, 3], [2, 3]]
t = [3, 2, 5]
x = Solution().minimumTime(n, r, t)
print(x)

n = 5
r = [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]]
t = [1, 2, 3, 4, 5]
x = Solution().minimumTime(n, r, t)
print(x)

