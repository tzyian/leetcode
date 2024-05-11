// https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array

'''
val -n-1 -n -n+1       0
ind  0    1  2  .. n
'''
# REDO

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def sum_arr(target: int) -> int:
            value = target
            count = 0
            if value > index:
                count += (value + value - index) * (index + 1) // 2
            else:
                count += (value + 1) * value // 2 + index - value + 1
        
            if value >= n - index:
                count += (value + value - n + 1 + index) * (n - index) // 2
            else:
                count += (value + 1) * value // 2 + n - index - value
            
            return count - value

            # total = 0
            # # first half
            # if target <= index:
            #     # extra 1s
            #     extras = index - target + 1
            #     total += extras
            #     total += target * (target + 1) // 2
            # else: 
            #     # shorter
            #     first = target - index
            #     count = target - first + 1
            #     total += (first + target) * count // 2
            # # second half including target index
            # if n - index <= target:
            #     # extra 1s
            #     extras = n - index - target
            #     total += extras
            #     total += target * (target + 1) // 2
            #     total -= target 
            # else: 
            #     diff = n - index
            #     last = target - diff
            #     total += (2 * target + (diff - 1) * - 1) * diff // 2 
            #     total -= target
            # return total
        

        
        def bsearch():
            l = 1
            h = maxSum
            while l < h:
                m = l + (h - l) // 2 + 1
                # I think they trying to get the ceiling instead of the floor
                # like if low = 0 and high =1 they want mid to be 1 and not 0
                if sum_arr(m) <= maxSum:
                    l = m
                else:
                    h = m - 1
            return l

        return bsearch()

        



                

            






