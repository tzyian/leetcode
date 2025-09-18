from typing import List


# @leet start
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # LIS will timeout, but you don't need to check all subsequences,
        # just the last value which fulfill the arithmetic subseq
        n = len(arr)
        dp = [1] * (n)
        ans = 1
        seen = dict()
        for i, x in enumerate(arr):
            if x - difference in seen:
                prev = seen[x - difference]
                dp[i] = 1 + dp[prev]
                ans = max(ans, dp[i])
            seen[x] = i  # must be after to prevent counting of i itself

        return ans


# @leet end

a = [1, 2, 3, 4]
d = 1
x = Solution().longestSubsequence(a, d)
print(x)

a = [1, 3, 5, 7]
d = 1
x = Solution().longestSubsequence(a, d)
print(x)

a = [1, 5, 7, 8, 5, 3, 4, 2, 1]
d = -2
x = Solution().longestSubsequence(a, d)
print(x)

