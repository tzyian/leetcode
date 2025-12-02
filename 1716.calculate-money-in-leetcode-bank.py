# @leet imports start
from typing import List, Optional

# @leet imports end


# @leet start
class Solution:
    def totalMoney(self, n: int) -> int:
        div, rem = divmod(n, 7)

        prev_weeks = (28 * div) + (7 * (div - 1) * div // 2)
        last_week = (rem * (rem + 1) // 2) + (rem * div)
        return prev_weeks + last_week


# @leet end

for n in (4, 10, 20):
    x = Solution().totalMoney(n)
    print(x)

