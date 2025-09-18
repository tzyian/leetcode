from math import cos, pi, sin, sqrt
from random import uniform
from typing import List

# NOTE: https://leetcode.com/problems/generate-random-point-in-a-circle/solutions/1113679/python-polar-coordinates-explained-with-diagrams-and-math/
# See the stats on why need sqrt
# Because a larger r circle increases area faster than smaller r circle
# Inverse transform sampling


# @leet start
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        R = self.r * sqrt(uniform(0, 1))
        theta = uniform(0, 2 * pi)
        return [self.x + R * cos(theta), self.y + R * sin(theta)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
# @leet end

