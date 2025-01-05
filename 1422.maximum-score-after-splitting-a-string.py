# @leet start
class Solution:
    def maxScore(self, s: str) -> int:
        # O(n) 2 pass
        n = len(s)
        num_ones = [0] * n
        psum = 0

        for i in range(n):
            if s[i] == "1":
                num_ones[i] = psum + 1
            else:
                num_ones[i] = psum
            psum = num_ones[i]

        # must be non-empty substring
        ans = 0
        num_zeroes = 0
        # i and before go to left
        for i in range(n - 1):
            if s[i] == "0":
                num_zeroes += 1
            ans = max(ans, num_zeroes + psum - num_ones[i])

        return ans


# @leet end

