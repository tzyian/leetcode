// https://leetcode.com/problems/check-if-it-is-a-straight-line

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n <= 2:
            return True
        c = coordinates
        m = gradient(c[0], c[1])
        for i in range(2, n):
            if gradient(c[0], c[i]) != m:
                return False
        return True


def gradient(p1, p2):
    dy = (p1[1] - p2[1]) 
    dx = (p1[0] - p2[0])
    if dx == 0:
        return float(inf)
    return dy/dx


