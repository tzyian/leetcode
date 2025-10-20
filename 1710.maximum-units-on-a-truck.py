# @leet imports start
from typing import *

# @leet imports end


# @leet start
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        ans = 0
        i = 0
        while truckSize > 0 and i < len(boxTypes):
            num, units = boxTypes[i]
            if num <= truckSize:
                truckSize -= num
                ans += num * units
                i += 1
            else:
                ans += truckSize * units
                return ans
        return -1


# @leet end

