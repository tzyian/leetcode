// https://leetcode.com/problems/minimum-speed-to-arrive-on-time

from typing import List
import math
# nlogn with binary search and n time each
class Solution:


    def finishable(self, spd: int, dist: List[int], hour: float) -> bool:
        # n time

        time_spent = 0
        for i in range(len(dist)):
            # float division
            # no ned to wait if the last stop
            if i == len(dist) - 1:
              time_spent += dist[i] / spd
            else:
                time_spent += math.ceil(dist[i] / spd)
        return time_spent <= hour





    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:        
        
        ## this edge case is WRONG!!!
        # # edge case where impossible to go on time
        # if sum(dist) > hour:
        #     return -1

        # binary search
        hi = 1e9 # go check what is a good val for hi
        lo = 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self.finishable(mid, dist, hour): 
                # if can be finished with mid, 
                # then check a lower speed, including mid
                hi = mid
            else:
                lo = mid + 1
        if self.finishable(lo, dist, hour):
            return int(lo)
        return -1
            