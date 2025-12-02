# @leet imports start

# @leet imports end

# TODO:
# very interesting implementation

# @leet start
class Solution:
    def maxOperations(self, s: str) -> int:
        # the end goal is 0..01..1
        ones = 0
        ans = 0
        for i, c in enumerate(s):
            if c == "1":
                ones += 1
            elif i > 0 and s[i - 1] == "1":
                ans += ones

        return ans


# @leet end

#    0123456
s = "1001101"
x = Solution().maxOperations(s)
print(x)

s = "00111"
x = Solution().maxOperations(s)
print(x)

