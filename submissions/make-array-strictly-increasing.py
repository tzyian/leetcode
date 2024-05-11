// https://leetcode.com/problems/make-array-strictly-increasing

from functools import cache

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)
        arr2.sort()
        n2 = len(arr2)
        inf = 2 << 32 - 1

        def smallest_greater_than(prev: int) -> int:
            # binary search O(logm)
            l, h = 0, n2 - 1
            while l < h:
                m = l + (h - l) // 2
                if arr2[m] <= prev:
                    l = m + 1
                elif arr2[m] > prev:
                    h = m
            if arr2[l] > prev:
                return arr2[l]
            else:
                return -1

        @cache
        # index is the value of the first index to be checked in the dp
        def helper(prev: int, index: int) -> int:
            if index == n:
                return 0

            rep_fr_a2 = smallest_greater_than(prev)
            replace = inf
            no_replace = inf

            if arr1[index] > prev:
                no_replace = helper(arr1[index], index + 1)
            if rep_fr_a2 > prev:
                replace = 1 + helper(rep_fr_a2, index + 1)
            return min(replace, no_replace)
            

        ans = helper(-1, 0)
        if ans == inf:
            return -1
        return ans


 
            
