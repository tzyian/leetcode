# @leet start
from typing import Counter, List

# Idea taken from editorial


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # O(n) Time, O(n) Space
        if len(hand) % groupSize != 0:
            return False

        c = Counter(hand)
        while c:
            k, v = next(iter(c.items()))
            # Get the root of any sequence
            while c[k - 1] > 0:
                k -= 1

            for j in range(groupSize):
                curr = k + j
                if c[curr] == 0:
                    return False
                c[curr] -= 1
                if c[curr] == 0:
                    del c[curr]

        return True


# @leet end
