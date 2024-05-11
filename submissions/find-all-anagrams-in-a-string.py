// https://leetcode.com/problems/find-all-anagrams-in-a-string

from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ls = len(s)
        lp = len(p)
        if ls < lp:
            return []

        ctr = Counter(p)
        roll = Counter(s[:lp])
        ans = []
        if roll == ctr:
            ans.append(0)
        "abcdefg" "bc"
        for i in range(1, ls-lp+1):
            roll = roll - Counter(s[i - 1]) + Counter(s[i+lp-1])
            if roll == ctr:
                ans.append(i)
        return ans