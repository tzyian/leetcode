from typing import List


# @leet start
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # the problem is this assumes a single uniform skew (all skew left or all skew right),
        # which is not the case
        # See the cpp solution

        n = len(nums1)
        m = len(nums2)
        dp = [0] * n
        last_i = -1
        last_j = -1
        for i in range(n):
            for j in range(min(i + 1, m)):
                if nums1[i] == nums2[j] and j > last_j and i > last_i:
                    dp[i] = max(dp[i], 1 + dp[i - 1])
                    last_i = i
                    last_j = j
                else:
                    dp[i] = max(dp[i], dp[i - 1])
        return dp[n - 1]


# @leet end

x = 0

a = [1, 4, 2]
b = [1, 2, 4]
x = Solution().maxUncrossedLines(a, b)  # 2
print(x)

a = [2, 5, 1, 2, 5]
b = [10, 5, 2, 1, 5, 2]
x = Solution().maxUncrossedLines(a, b)  # 3
print(x)

a = [1, 3, 7, 1, 7, 5]
b = [1, 9, 2, 5, 1]
x = Solution().maxUncrossedLines(a, b)  # 2
print(x)

a = [2, 3, 1]
b = [3, 1, 3, 3, 3, 3]
# where 2-1 3-1 means you cant just skew left
x = Solution().maxUncrossedLines(a, b)  # 2
print(x)

a = [2, 1]
b = [1, 2, 1, 3, 3, 2]
# where 2-2 prevents 1-1 from occurring
x = Solution().maxUncrossedLines(a, b)  # 2
print(x)

