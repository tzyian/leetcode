from typing import List


# @leet start
class Solution:
    def trap(self, height: List[int]) -> int:
        # O(n) TC
        # O(n) SC to build the prefix and suffix arrays
        n = len(height)
        if n <= 1:
            return 0

        water = 0
        highest_to_left = [height[0]]
        for i in range(1, n):
            next = max(highest_to_left[i - 1], height[i])
            highest_to_left.append(next)

        highest_to_right = [height[n - 1]]
        for i in range(1, n):
            next = max(highest_to_right[i - 1], height[n - 1 - i])
            highest_to_right.append(next)
        highest_to_right = list(reversed(highest_to_right))

        for i in range(n):
            water += min(highest_to_right[i], highest_to_left[i]) - height[i]

        return water


# @leet end

ls = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
y = Solution().trap(ls)
print(y)
ls = [4, 2, 0, 3, 2, 5]
x = Solution().trap(ls)
print(x)

