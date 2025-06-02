# @leet start
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        total = 0

        for i in range(min(limit, n) + 1):
            if n - i > 2 * limit:
                continue
            upper = min(n - i, limit)
            lower = max(0, n - i - limit)
            total += upper - lower + 1
        return total


# @leet end

n = 5
l = 2
x = Solution().distributeCandies(n, l)
print(x)  # 3

n = 3
l = 3
x = Solution().distributeCandies(n, l)
print(x)  # 10

n = 100
l = 1
x = Solution().distributeCandies(n, l)
print(x)  # 0

