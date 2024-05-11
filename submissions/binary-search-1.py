// https://leetcode.com/problems/binary-search

class Solution:
    from bisect import bisect_left
    def search(self, nums: List[int], target: int) -> int:
        ind = bisect_left(nums, target)
        if ind < 0 or ind >= len(nums) or nums[ind] != target:
            return -1
        return ind

        