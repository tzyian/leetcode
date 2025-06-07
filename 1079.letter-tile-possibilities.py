# @leet start
from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # Same as 47. Permutations II
        ctr = Counter(tiles)

        ans = 0

        def backtrack():
            nonlocal ans

            for c in ctr:
                if ctr[c] > 0:
                    ans += 1
                    ctr[c] -= 1
                    backtrack()
                    ctr[c] += 1

        backtrack()
        return ans


# @leet end
t = "AAB"
t = "AAABBC"
t = ""
x = Solution().numTilePossibilities(t)
print(x)
