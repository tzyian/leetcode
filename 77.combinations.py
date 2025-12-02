# @leet imports start
from typing import List

# @leet imports end


# @leet start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(start: int, curr: List[int]) -> None:
            if len(curr) == k:
                ans.append(curr[:])

            for i in range(start, n + 1):
                curr.append(i)
                backtrack(i + 1, curr)
                curr.pop()

        backtrack(1, [])
        return ans


# @leet end

n = 4
k = 2
x = Solution().combine(n, k)
print(x)

