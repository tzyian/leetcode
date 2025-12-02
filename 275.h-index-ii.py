# @leet imports start
from typing import List

# @leet imports end


"""
h-index:

For every index i, we find a value h such that
(1) there are at least h−1 papers strictly after i, and
(2) the current paper has at least h citations,
Then we find the max h for all i

i.e.
For each i,
    h <= n - i        i.e.  i <= n - h
    h <= citations[i]
Find max_i of h


since the array is sorted, we just need to check 
i = 0,1,2,...n-h
citations[i] <= citations[i+1] <= ... <= citations[n-h]


### Finding the condition for i
To turn i <= n - h into i = n - h,
citations[i] >= h is satisfied for some index i_0

If this is a valid range, then i \in [i_0, n-h]
We check i = n-h because citations[n-h] >= citations [i_0]
and citations[n-h] is more likely to fulfill the criterion within this valid range
Formally, citations[n − h] ≥ citations[i] ≥ h
So i = n - h


So now the condition is reduced to
h <= citations[n - h]

mid = h, since if a paper fulfills the criteria, there are h-1 papers after it,
so we don't need to bsearch on the [0, max(citations)] instead 
(which we can't anyway cos some citation numbers don't exit)

and the condition is 
return h <= citations[n - h]

this condition checks suffixes of length h
T T T T F F F
where the last T means 

put another way:

A researcher has H-index h if and only if
at least h papers have ≥ h citations,
and
fewer than h+1 papers have ≥ h+1 citations.
"""


# @leet start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 0, 1, 2, 3, 4
        n = len(citations)

        def valid(h: int) -> bool:
            # find the last valid
            if h == 0:
                # this must be included because h == 0 is always true
                # and the range of 0 papers to 0 papers is undefined
                # so needs to be special cased
                # citations[1-0] = citations[1] is out of bound
                return True
            return h <= citations[n - h]

        lo = 0
        hi = n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if valid(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo - 1


# @leet end

arr = [0, 0, 4, 4]
x = Solution().hIndex(arr)
print(x)

