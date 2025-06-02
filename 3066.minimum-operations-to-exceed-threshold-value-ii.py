from heapq import heapify, heappop, heappush
from typing import List


# @leet start
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # SC O(n) from heap
        # TC O(nlogn). O(n) from heapify,
        # up to n * logn heappops can be done (and answer guaranteed to exist)
        heapify(nums)
        count = 0
        while nums[0] < k:
            count += 1
            x = heappop(nums)
            y = heappop(nums)
            heappush(nums, x * 2 + y)
        return count


# @leet end

