# @leet imports start
from typing import List, Optional

# @leet imports end


# @leet start
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        # RED HERRING
        # you want to overlap the planting time and growing time as much as possible
        # make as many plants grow in parallel as possible
        # there is no reason to break apart the planting of a seed

        # also note that the solution is lower bounded (but not nec achievable)
        # sum(plantTime) + min(growTime)
        # starting from the last plant planted,
        # so if we remove the min(growTime), then we have plantTime left

        plants = sorted(zip(plantTime, growTime), key=lambda x: (-x[1], -x[0]))
        bloom = 0
        today = 0
        for pl, gr in plants:
            today += pl
            bloom = max(bloom, today + gr)

        return bloom


# @leet end

p = [1, 4, 3]
g = [2, 3, 1]
x = Solution().earliestFullBloom(p, g)
print(x)

[1, 2, 3, 2]
[2, 1, 2, 1]

[1]
[1]

