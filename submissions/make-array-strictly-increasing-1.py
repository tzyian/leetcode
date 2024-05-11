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

            if arr1[index] <= prev and rep_fr_a2 != -1:
                return 1 + helper(rep_fr_a2, index + 1)
            elif arr1[index] <= prev and rep_fr_a2 == -1:
                return inf
            elif arr1[index] > prev and rep_fr_a2 == -1:
                return helper(arr1[index], index + 1)
            elif arr1[index] > prev and rep_fr_a2 != -1:
                no_r = helper(arr1[index], index + 1)
                r = helper(rep_fr_a2, index + 1)
                if r != inf and no_r != inf:
                    return min(1 + r, no_r)
                elif r != inf:
                    return 1 + r
                elif no_r != inf:
                    return no_r
                else:
                    return inf
            

        ans = helper(-1, 0)
        if ans > 2000:
            return -1
        return ans


 
            
