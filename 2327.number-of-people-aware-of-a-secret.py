# @leet start
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        # dp[i][j] = ppl who have known secret for j + 1 days at day i
        MOD = 10**9 + 7

        dp = [[0] * (forget + 1) for _ in range(n + 1)]

        dp[1][1] = 1

        for i in range(2, n + 1):
            for j in range(2, 1 + forget):
                dp[i][j] = dp[i - 1][j - 1]
                if j >= 1 + delay:
                    dp[i][1] = (dp[i][1] + dp[i][j]) % MOD

        return sum(i for i in dp[n][1:]) % MOD


# @leet end

n = 6
d = 2
f = 4
x = Solution().peopleAwareOfSecret(n, d, f)
print(x)

n = 4
d = 1
f = 3
x = Solution().peopleAwareOfSecret(n, d, f)
print(x)

