from typing import List


# @leet start
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))

        tot = 0
        n = len(points)
        for i in range(n):
            _, y1 = points[i]
            highest_y = -1
            for j in range(i + 1, n):
                _, y2 = points[j]
                if highest_y <= y2 <= y1:
                    tot += 1
                    highest_y = max(highest_y, y2)

        return tot


# @leet end
