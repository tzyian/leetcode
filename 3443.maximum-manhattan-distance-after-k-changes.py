# @leet start
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        dy = 0
        dx = 0
        ans = 0
        n = len(s)

        for i in range(n):
            match s[i]:
                case "N":
                    dy += 1
                case "S":
                    dy -= 1
                case "E":
                    dx += 1
                case "W":
                    dx -= 1
            # Must do min(i + 1) here
            mdist = min(abs(dx) + abs(dy) + k * 2, i + 1)
            ans = max(ans, mdist)

        return ans


# @leet end

