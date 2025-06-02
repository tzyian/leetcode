# @leet start
from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        c = Counter(s)
        ans = 0

        for v in c.values():
            if v & 1:
                ans += 1
            else:
                ans += 2

        return ans

        
# @leet end
