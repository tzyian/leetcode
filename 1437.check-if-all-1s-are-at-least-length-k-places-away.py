# @leet imports start
from typing import List, Optional

# @leet imports end


# @leet start
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        inf = 10**10
        last_one = -inf
        for i, x in enumerate(nums):
            if x == 1:
                # 0, 4 are 2 places from each other
                if i - 1 - last_one < k:
                    return False
                last_one = i
        return True


# @leet end

