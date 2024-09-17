# @leet start

from collections import Counter
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c1 = Counter(s1.split())
        c2 = Counter(s2.split())
        return [k for k, v in (c1 + c2).items() if v == 1]


# @leet end
