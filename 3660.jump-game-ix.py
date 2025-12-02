# @leet imports start
from typing import List, Optional

# @leet imports end

# NOTE: not working!


# @leet start
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        # 5 ... 1
        # i     j   can jump fwd if fwd is smaller

        # 5     1
        # j     i   can jump back if back is higher

        # 5 2 1 8 3
        # 2 -> 5 -> 3 -> 8
        # for every element, find the largest element before it
        # for every element, it can go to any smaller element after it and jump back

        n = len(nums)

        largest_idx_before = 0
        largest_before = [0] * n
        for i in range(n):
            if nums[i] >= nums[largest_idx_before]:
                largest_idx_before = i
            largest_before[i] = largest_idx_before

        ans = [0] * n
        for i in range(n):
            ans[i] = nums[largest_before[smallest_after[i]]]

        return ans


# @leet end

nums = [2, 1, 3]
x = Solution().maxValue(nums)
print(x)

nums = [30, 21, 5, 35, 24]
x = Solution().maxValue(nums)
print(x)  # [35,35,35,35,35]

