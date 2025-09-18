from typing import List

# compare this question to 377. Combination Sum IV
# which wants ordered combinations,
# while this wants unordered combinations


# @leet start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        # loop over coins first to avoid counting permutations
        # for each coin, loop over all amounts from coin to amount
        # so no need to check i - coin >= 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]


# @leet end


class SolutionUnopt:
    # not space optimised
    def changeSpace(self, amount: int, coins: List[int]) -> int:
        # dp[i][j] = number of ways to make $i using any multiples of first j coins
        # dp[0][j] = make $0
        # dp[i][0] = make using no coins
        m = len(coins)
        dp = [[0] * (m + 1) for _ in range(amount + 1)]

        # 1 way to make $0
        for j in range(m + 1):
            dp[0][j] = 1

        for i in range(1, amount + 1):
            for j in range(1, m + 1):
                not_use = dp[i][j - 1]
                if i >= coins[j - 1]:
                    use = dp[i - coins[j - 1]][j]
                else:
                    use = 0
                dp[i][j] = use + not_use
        return dp[amount][m]


a = 5
c = [1, 2, 5]
x = Solution().change(a, c)
print(x)
