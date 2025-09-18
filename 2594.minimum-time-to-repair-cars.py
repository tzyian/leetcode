from typing import List


# @leet start
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def can_repair_in_time(time: int) -> bool:
            total_cars = 0
            for rank in ranks:
                total_cars += int((time // rank) ** 0.5)
                if total_cars >= cars:
                    return True
            return False

        # actually, min_rank is a tighter upper bound
        # with min_rank (faster) repairing all cars by themself
        max_rank = max(ranks)
        lo = 1
        hi = max_rank * cars * cars + 1
        while lo < hi:
            mid = (lo + hi) // 2
            if can_repair_in_time(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo


# @leet end

ranks = [1, 100]
cars = 2
print(Solution().repairCars(ranks, cars))
