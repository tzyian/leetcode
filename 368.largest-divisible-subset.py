from typing import List


# @leet start
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dp = [1] * n
        parent = [-1] * n
        max_len = 1
        max_index = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j
            if dp[i] > max_len:
                max_len = dp[i]
                max_index = i

        # rebuild the subset using the parent
        ans = []
        while max_index != -1:
            ans.append(nums[max_index])
            max_index = parent[max_index]
        return ans[::-1]


# @leet end
