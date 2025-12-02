# @leet imports start
from typing import List, Optional

# @leet imports end


# @leet start
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        empty = numBottles
        drank = numBottles
        while empty >= numExchange:
            empty -= numExchange
            drank += 1
            empty += 1
            numExchange += 1

        return drank


# @leet end

n = 13
ne = 6
x = Solution().maxBottlesDrunk(n, ne)
print(x)

