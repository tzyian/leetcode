# @leet start
from collections import Counter


class Solution:
    def maxFreqSum(self, s: str) -> int:
        c = Counter(s)
        cons = 0
        vows = 0
        for k, v in c.most_common():
            if k in ("a", "e", "i", "o", "u"):
                if vows == 0:
                    vows = v
            elif cons == 0:
                cons = v
        return cons + vows


# @leet end

