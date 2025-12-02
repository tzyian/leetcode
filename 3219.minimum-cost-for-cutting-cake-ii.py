# @leet imports start
from typing import List, Optional

# @leet imports end

# NOTE: recognising that it is greedy is the difficult part


# @leet start
class Solution:
    def minimumCost(
        self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]
    ) -> int:
        ans = 0
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        h = 0
        v = 0
        while h < m - 1 and v < n - 1:
            if horizontalCut[h] > verticalCut[v]:
                ans += horizontalCut[h] * (v + 1)
                h += 1
            else:
                ans += verticalCut[v] * (h + 1)
                v += 1

        while h < m - 1:
            ans += horizontalCut[h] * (v + 1)
            h += 1

        while v < n - 1:
            ans += verticalCut[v] * (h + 1)
            v += 1

        return ans


# @leet end

m = 3
n = 2
hc = [1, 3]
vc = [5]
x = Solution().minimumCost(m, n, hc, vc)
print(x)

2
2
[7]
[4]

