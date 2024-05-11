// https://leetcode.com/problems/check-if-array-is-sorted-and-rotated

class Solution:
    def check(self, nums: List[int]) -> bool:
        return sum(nums[i] < nums[i-1] for i in range(len(nums))) <= 1