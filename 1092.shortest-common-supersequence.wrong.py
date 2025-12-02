# @leet start
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)

        # NOTE: mem exceeded
        # TC is (n*m) * (n+m),
        # from the table * concatenation
        # SC is (n*m) * (n+m)
        # from table * strlen

        if n == 0:
            return str2
        if m == 0:
            return str1
        if str1 == str2:
            return str1

        dp = [["" for _ in range(m + 1)] for _ in range(n + 1)]

        # build up the first row and first col with a string of all chars up to i/j
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + str1[i - 1]
        for j in range(1, m + 1):
            dp[0][j] = dp[0][j - 1] + str2[j - 1]

        # dp[i][j] = shortest superseq from s1[:i] and s2[:j]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
                else:
                    from_s1 = dp[i - 1][j]
                    from_s2 = dp[i][j - 1]
                    if len(from_s1) < len(from_s2):
                        dp[i][j] = from_s1 + str1[i - 1]
                    else:
                        dp[i][j] = from_s2 + str2[j - 1]

        return dp[n][m]


# @leet end

s1 = "abac"
s2 = "cab"
x = Solution().shortestCommonSupersequence(s1, s2)
print(x)
