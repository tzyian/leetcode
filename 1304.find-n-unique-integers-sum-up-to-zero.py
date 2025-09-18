from typing import List


# @leet start
class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        for i in range(1, n // 2 + 1):
            ans.append(i)
            ans.append(-i)
        if n & 1 == 1:
            ans.append(0)
        return ans


# @leet end

n = 5
x = Solution().sumZero(n)
print(x)

