from typing import List


# @leet start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()  # so you can skip
        n = len(nums)

        def dfs(first: int, curr: list[int]):
            ans.append(curr[:])

            for i in range(first, n):
                # subset2 specific things
                if i > first and nums[i] == nums[i - 1]:
                    continue
                # end
                curr.append(nums[i])
                dfs(i + 1, curr)
                curr.pop()

        dfs(0, [])
        return ans


# @leet end
