# https://leetcode.com/problems/combination-sum/
from typing import List


# @leet start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []
        candidates.sort()

        def dfs(start: int, curr: list[int], tot: int) -> None:
            if tot == target:
                ans.append(curr[:])

            for i in range(start, n):
                num = candidates[i]
                if tot + num > target:
                    return

                curr.append(num)
                dfs(i, curr, tot + num)
                curr.pop()

        dfs(0, [], 0)
        return ans


# @leet end
c = [2, 3, 6, 7]
t = 7
x = Solution().combinationSum(c, t)
print(x)

c = [2, 3, 5]
t = 8
x = Solution().combinationSum(c, t)
print(x)

c = [2]
t = 1
x = Solution().combinationSum(c, t)
print(x)

c = [8, 7, 4, 3]
t = 11
x = Solution().combinationSum(c, t)
print(x)
