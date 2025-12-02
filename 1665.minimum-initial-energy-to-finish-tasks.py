# @leet imports start
from typing import List, Optional

# @leet imports end


# @leet start
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # largest difference first
        # because this gives the most leftovers for the remaining tasks
        tasks.sort(key=lambda a: a[1] - a[0], reverse=True)

        ans = 0
        curr = 0

        for actual, minimum in tasks:
            if curr >= minimum:
                curr -= actual  # use stored value
                continue

            ans += minimum - curr  # top up the difference
            curr = minimum - actual

        return ans


# @leet end

t = [[1, 2], [2, 4], [4, 8]]
x = Solution().minimumEffort(t)
print(x)

