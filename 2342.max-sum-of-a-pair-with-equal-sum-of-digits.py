# @leet start
from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # Ok i forgot that heaps are only strictly ordered
        # across levels but not within levels.
        # heap[0] <= heap[1], heap[2], but heap[1] need not <= heap[2]
        # So you can't use a minheap and take the first two elements
        # But you can use a maxheap and pop all the smallest elements

        # the suggested answer is that since you only need to know the largest element for a given digit sum,
        # there is no need to use a heap for digit sum,
        # and you can compute the number sum for each element you iterate through
        # but this has the same TC

        best_sum = -1
        digit_sums = defaultdict(list)
        for num in nums:
            dsum = sum(int(d) for d in str(num))
            heap = digit_sums[dsum]
            heappush(heap, num)
            if len(heap) > 2:
                heappop(heap)
            if len(heap) == 2:
                best_sum = max(best_sum, heap[0] + heap[1])
        return best_sum


# @leet end


ls = [18, 43, 36, 13, 7]
ls = [10, 12, 19, 14]
ls = [
    229,
    398,
    269,
    317,
    420,
    464,
    491,
    218,
    439,
    153,
    482,
    169,
    411,
    93,
    147,
    50,
    347,
    210,
    251,
    366,
    401,
]  # 973. test that you recall the heap partially ordered invariant
x = Solution().maximumSum(ls)
print(x)

