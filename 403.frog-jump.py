# @leet imports start
from collections import deque
from typing import *

# @leet imports end


# @leet start
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        n = len(stones)

        # dp[i][j] = True/False for can reach
        # where i is the stone index, 0 to n-1
        # j is the jump it took to jump to a stone k
        # since j0=0,j1 = 1, j2 = 2, ... jn-1 = n-1
        # so j caps at n-1

        # we check jump dist to at most dist + 1
        dp = [[False] * (n + 1) for _ in range(n)]
        dp[0][0] = True  # to get to the 0th spot, you took a jump of 0
        for i in range(1, n):  # the current stone
            for j in range(i):  # any previous stone
                dist = stones[i] - stones[j]
                if dist > n - 1:  # i cannot be reached from j in 1 jump
                    continue
                if dp[j][dist] or dp[j][dist - 1] or dp[j][dist + 1]:
                    dp[i][dist] = True
                    if i == n - 1:
                        return True

        return False

    def canCrossDfs(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        posts = set(stones)

        stack = []
        stack.append((1, 1))
        visited = set()
        while stack:
            pos, jump = stack.pop()
            visited.add((pos, jump))
            if pos == stones[-1]:
                return True
            for d in (1, 0, -1):
                next = pos + jump + d
                if next in posts and (next, jump + d) not in visited:
                    stack.append((next, jump + d))

        return False


# @leet end

x = ""
stones = [0, 1, 3, 5, 6, 8, 12, 17]
# x = Solution().canCross(stones)
print(x)

stones = [0, 1, 2, 5, 6, 9, 10, 12, 13, 14, 17, 19, 20, 21, 26, 27, 28, 29, 30]
x = Solution().canCross(stones)
print(x)

