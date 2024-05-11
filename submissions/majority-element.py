// https://leetcode.com/problems/majority-element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        floor = len(nums) // 2
        x = Counter(nums)
        for i in x:
            if x[i] > floor:
                return i