// https://leetcode.com/problems/set-mismatch

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = [-1, -1]
        for i, ele in enumerate(nums):
            if nums[abs(ele) - 1] > 0:
                nums[abs(ele) - 1] = -nums[abs(ele) - 1]
            else:
                ans[0] = abs(ele)
        for i, ele in enumerate(nums):
            if ele > 0:
                ans[1] = i+1
        return ans
        


        