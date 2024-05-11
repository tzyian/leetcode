// https://leetcode.com/problems/valid-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ls = Counter(s)
        for i in t:
            if i in ls and ls[i] > 0:
                ls[i] -= 1
            else:
                return False
        return True