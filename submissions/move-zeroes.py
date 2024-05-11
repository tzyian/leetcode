// https://leetcode.com/problems/move-zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        # destructively get rid of 0s

        def swap(a, b):
            nums[a], nums[b] = nums[b], nums[a]

        slow = 0
        for fast in range(1, n):
            while nums[slow] != 0 and slow < fast:
                slow += 1
            if nums[fast] != 0:
                swap(fast, slow)
                slow += 1
        print(nums)





        