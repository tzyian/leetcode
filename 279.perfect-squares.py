# NOTE: Lagrange four-square theorem states that every natural number can be represented as the sum of four integer squares.

# @leet start
from math import isqrt


class Solution:
    def numSquares(self, n: int) -> int:
        # BFS
        max_sq = isqrt(n)
        squares = [x**2 for x in range(max_sq + 1)]

        queue = [n]
        depth = 0
        seen = set()
        while queue:
            depth += 1
            x = len(queue)
            for _ in range(x):
                num = queue.pop(0)
                for sq in squares:
                    next_num = num - sq
                    if next_num < 0:
                        break
                    if next_num == 0:
                        return depth
                    if next_num not in seen:
                        seen.add(next_num)
                        queue.append(next_num)
        return -1


# @leet end


class Solution1d:
    def numSquares(self, n: int) -> int:
        # dp[i] = number of squares which sums to i
        # dp[i] = min(dp[i - prev_sq] + 1 for prev_sq in squares if i - prev_sq >= 0)
        max_sq = isqrt(n)
        squares = [x**2 for x in range(max_sq + 1)]

        inf = 10**8

        dp = [inf] * (n + 1)
        dp[0] = 0

        # this works because we are looking for minimum number of squares
        # so order of squares doesn't matter
        # we can build up from smaller numbers to larger numbers
        # similar to coin change 1
        for i in range(1, n + 1):
            for sq in squares:
                if i - sq >= 0:
                    dp[i] = min(dp[i], dp[i - sq] + 1)

        return dp[n]


class Solution2d:
    def numSquares(self, n: int) -> int:
        # dp[i][j] = number of squares which sums to i with the first j primes
        # skip = dp[i][j-1]
        # take = dp[i - prev_sq][j]
        # TODO: there are more optimised solutions
        max_sq = isqrt(n)
        squares = [x**2 for x in range(max_sq + 1)]

        inf = 10**8

        dp = [[inf] * (max_sq + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for j in range(max_sq + 1):
            dp[0][j] = 0

        for i in range(1, n + 1):
            for j in range(1, max_sq + 1):
                skip = dp[i][j - 1]
                if i - squares[j] >= 0:
                    take = dp[i - squares[j]][j] + 1
                else:
                    take = inf
                dp[i][j] = min(skip, take)

        return dp[n][max_sq]


n = 12
x = Solution().numSquares(n)
print(x)
n = 13
x = Solution().numSquares(n)
print(x)

