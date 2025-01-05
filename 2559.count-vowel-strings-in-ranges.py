# @leet start
from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # O(n) time, O(n) space where n = len(words)

        if not queries or not words:
            return []

        vowels = ["a", "e", "i", "o", "u"]
        n = len(words)
        fulfill = lambda w: w[0] in vowels and w[-1] in vowels
        bools = [fulfill(w) for w in words]

        psums = [0] * n
        psums[0] = 0 + bools[0]
        for i in range(1, n):
            psums[i] = psums[i - 1] + bools[i]

        ans = []
        for l, r in queries:
            count = psums[r] - psums[l] + bools[l]
            ans.append(count)

        return ans


# @leet end

