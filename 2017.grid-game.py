# @leet start
from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])

        # ok you don't actually need to store the psum/ssum
        ss0 = grid[0].copy()
        ps1 = grid[1].copy()

        for i in range(1, n):
            ss0[n - 1 - i] += ss0[n - i]
            ps1[i] += ps1[i - 1]

        ans = float("inf")
        for i in range(n):
            top_ss = 0
            bot_ss = 0
            if i < n - 1:
                top_ss = ss0[i + 1]
            if i > 0:
                bot_ss = ps1[i - 1]
            ans = min(ans, max(top_ss, bot_ss))
        return int(ans)


# @leet end

