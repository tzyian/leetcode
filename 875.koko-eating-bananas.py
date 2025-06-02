from typing import List


# @leet start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)

        def can_finish(speed: int) -> bool:
            curr_hour = 0
            for pile in piles:
                if pile % speed == 0:
                    curr_hour += pile // speed
                else:
                    curr_hour += pile // speed + 1

            if curr_hour > h:
                return False
            return True

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if can_finish(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo


# @leet end

