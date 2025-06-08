from typing import List


# @leet start
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # 1 10 100 1000 10_000 10_001...10_0009 10_0010
        ans = []
        curr = 1

        for _ in range(n):
            ans.append(curr)
            if curr * 10 <= n:
                curr *= 10
            else:
                while curr % 10 == 9 or curr >= n:
                    curr //= 10
                curr += 1

        return ans


# @leet end

n = 13
x = Solution().lexicalOrder(n)
print(x)

