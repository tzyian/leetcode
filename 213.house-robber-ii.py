from typing import List


# @leet start
class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def helper(nums: List[int]) -> int:
            take = 0
            notake = 0
            n = len(nums)

            for i in range(n):
                temp = take
                take = notake + nums[i]
                notake = max(temp, notake)
            return max(take, notake)

        return max(helper(nums[1:]), helper(nums[: len(nums) - 1]))


# @leet end

nums = [1]
x = Solution().rob(nums)
print(x)

