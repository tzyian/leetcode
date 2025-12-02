# @leet imports start
from typing import List, Optional

# @leet imports end


from bisect import bisect_left, bisect_right


# @leet start
class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        sort_sp = sorted((s, i) for (i, s) in enumerate(spells))
        potions.sort()
        ans = []
        n = len(potions)

        highest = n
        for spell, i in sort_sp:
            res = bisect_left(potions, success, 0, highest, key=lambda p: p * spell)
            highest = min(res + 1, n)
            ans.append((i, n - res))
        ans.sort(key=lambda x: x[0])
        return [r for _, r in ans]


# @leet end

x = ""
s = [5, 1, 3]
p = [1, 2, 3, 4, 5]
su = 7
x = Solution().successfulPairs(s, p, su)
print(x)

s = [1, 2, 3]
p = [5, 8, 8]
su = 16
x = Solution().successfulPairs(s, p, su)
print(x)

