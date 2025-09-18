from typing import List
from random import randint


# @leet start
class Solution:

    def __init__(self, nums: List[int]):
        self.orig = nums[:]
        self.nums = nums

    def reset(self) -> List[int]:
        self.nums = self.orig[:]
        return self.nums

    def shuffle(self) -> List[int]:
        nums = self.nums
        n = len(nums)

        for i in range(n - 1):
            a = randint(i, n - 1)
            nums[i], nums[a] = nums[a], nums[i]
        return nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @leet end

