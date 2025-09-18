from typing import List


# @leet start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        maxseen = nums[i]
        while i <= min(maxseen, n - 1):
            maxseen = max(nums[i] + i, maxseen)
            i += 1

        return maxseen >= n - 1


# @leet end

n = [2, 3, 1, 1, 4]
x = Solution().canJump(n)
print(x)

n = [3, 2, 1, 0, 4]
x = Solution().canJump(n)
print(x)

n = [1, 1, 1, 1, 1, 1]
x = Solution().canJump(n)
print(x)

