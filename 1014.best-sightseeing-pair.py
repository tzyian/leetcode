# @leet start
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)

        best_left = values[0] + 0
        best_score = -1

        for i in range(1, n):
            best_left = max(best_left, values[i - 1] + i - 1)
            best_score = max(best_score, best_left + values[i] - i)

        return best_score


# @leet end

values = [8, 1, 5, 2, 6]
values = [1, 2]
ans = Solution().maxScoreSightseeingPair(values)
print(ans)
