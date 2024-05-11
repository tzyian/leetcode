// https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)
        if n <= 2:
            return True

        minv = min(arr)
        maxv = max(arr)
        if (maxv - minv) % (n - 1):
            return False
        # you cant use arr[0] - arr[1] because 2,4,3,5 wont give correct diff
        d = (maxv - minv) // (n - 1)
        if d == 0:
            return True

        checked = 0
        minind = arr.index(minv)
        arr[minind], arr[0] = arr[0], arr[minind]
        seen = set()
        while checked < n:
            if arr[checked] == minv + checked * d:
                checked += 1
                continue
            elif (arr[checked] - minv) % d != 0:
                return False
            currv = arr[checked]
            corr_ind = (currv - minv) // d
            if corr_ind < 0 or corr_ind >= n or \
            arr[checked] == arr[corr_ind]:
                return False
            arr[checked], arr[corr_ind] = arr[corr_ind], arr[checked]
            prev_ind = corr_ind
        return True


    
