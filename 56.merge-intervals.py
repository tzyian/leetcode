# @leet start
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)

        intervals.sort()
        prev_start, prev_end = intervals[0]
        ans = []
        for i, (curr_start, curr_end) in enumerate(intervals):
            if prev_end >= curr_start:
                prev_end = max(prev_end, curr_end)
                if i == n - 1:
                    ans.append([prev_start, prev_end])
            elif prev_end < curr_start:
                ans.append([prev_start, prev_end])
                if i == n - 1:
                    ans.append([curr_start, curr_end])
                prev_start, prev_end = curr_start, curr_end

        return ans


# @leet end
