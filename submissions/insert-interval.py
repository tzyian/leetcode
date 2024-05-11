// https://leetcode.com/problems/insert-interval

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        # Skip intervals that end before the new interval starts
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Merge intervals that overlap with the new interval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Append the merged new interval
        result.append(newInterval)

        # Append remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        return result