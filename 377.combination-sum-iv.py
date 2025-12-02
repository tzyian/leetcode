from typing import List

# combinationSum4 is ordered (permutations)
## loop over target first to allow double counting
## before looping over coins

# 518. Coin Change II is unordered (combinations)
## loop over coins first to prevent double counting


# if there are -ve numbers,
# there needs to be a restriction on number of uses for each number


# @leet start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for x in nums:
                if i - x >= 0:
                    dp[i] += dp[i - x]

        return dp[target]


# @leet end
x = ""
n = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 2, 2],
    [1, 2, 3],
    [1, 3, 4],
]

n = [1, 2, 3]
t = 4
x = Solution().combinationSum4(n, t)
print(x)

n = [9]
t = 3
x = Solution().combinationSum4(n, t)
print(x)
