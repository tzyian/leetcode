from typing import List


# @leet start
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        s = set()

        for i in range(n - 1, -1, -1):
            if nums[i] in s:
                if (i + 1) % 3 == 0:
                    return (i + 1) // 3
                else:
                    return (i + 1) // 3 + 1
            else:
                s.add(nums[i])
        
        return 0
# @leet end
