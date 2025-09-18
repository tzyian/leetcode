from typing import List


# @leet start
class Solution:
    def jump(self, nums: List[int]) -> int:
        # if you can reach i in n jumps, you can reach all j < i in n jumps
        # use 2 pointers for this (I did not get this idea)
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 1
        l = 0
        r = nums[0]
        furthest = nums[0]
        while furthest < n - 1:
            while l <= r:
                furthest = max(l + nums[l], furthest)
                l += 1
            r = furthest
            jumps += 1

        return jumps


# @leet end

n = [2, 3, 1, 1, 4]
x = Solution().jump(n)
print(x)

n = [2, 3, 0, 1, 4]
x = Solution().jump(n)
print(x)

