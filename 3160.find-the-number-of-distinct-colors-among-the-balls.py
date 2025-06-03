from collections import defaultdict
from typing import List


# @leet start
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        result = []
        colours = defaultdict(int)
        balls = dict()
        for b, c in queries:
            if b not in balls:
                balls[b] = c
                colours[c] += 1
            else:
                existing = balls[b]
                balls[b] = c

                colours[c] += 1

                colours[existing] -= 1
                if colours[existing] == 0:
                    del colours[existing]

            result.append(len(colours))

        return result


# @leet end

