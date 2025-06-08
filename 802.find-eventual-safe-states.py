from typing import List


# @leet start
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # to deal with cycles as well
        # also deal with 1 -> 2 -> 3, 1->3

        n = len(graph)
        is_safe = [False] * n
        in_path = [False] * n

        def dfs(i: int, in_path: list[bool]) -> bool:

            if not graph[i]:
                is_safe[i] = True
                return True
            if in_path[i]:
                is_safe[i] = False
                return False
            if is_safe[i]:
                return True

            for nb in graph[i]:
                in_path[i] = True
                seems_safe = dfs(nb, in_path)
                in_path[i] = False
                if seems_safe:
                    continue
                else:
                    return False

            is_safe[i] = True
            return True

        for i in range(n):
            dfs(i, in_path)
        return [i for i, b in enumerate(is_safe) if b == True]


# @leet end

g = [[1, 2], [2, 3], [5], [0], [5], [], []]
g = [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]
x = Solution().eventualSafeNodes(g)
print(x)

