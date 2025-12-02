from typing import List


# @leet start
class Solution:
    def canJumpReverse(self, nums: List[int]) -> bool:
        # moving the goalpost backwards
        n = len(nums)
        to_reach = n - 1
        for j in range(n - 1, -1, -1):
            if j + nums[j] >= to_reach:
                to_reach = min(to_reach, j)
        return to_reach == 0

    def canJump(self, nums: List[int]) -> bool:
        # moving forward, tracking the max reachable index
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
