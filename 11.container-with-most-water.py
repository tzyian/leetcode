# @leet start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        l = 0
        r = n - 1
        most = 0

        while l < r:
            water = (r - l) * min(height[l], height[r])
            most = max(water, most)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return most


# @leet end
