from typing import List


# @leet start
class Solution:
    def rob(self, nums: List[int]) -> int:
        take = 0
        notake = 0

        n = len(nums)
        for i in range(n):
            temp = take
            take = notake + nums[i]
            notake = max(temp, notake)
        return max(take, notake)


# @leet end

n = [1, 1, 3, 3]
n = [2, 9, 8, 3, 6]
x = Solution().rob(n)
print(x)

