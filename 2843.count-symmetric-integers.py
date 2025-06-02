# @leet start
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for num in range(low, high + 1):
            if num < 100 and num % 11 == 0:
                ans += 1
            elif 1001 <= num <= 9999:
                lhs = num // 1000 + num % 1000 // 100
                rhs = num % 100 // 10 + num % 10
                if lhs == rhs:
                    ans += 1
        return ans


# @leet end

