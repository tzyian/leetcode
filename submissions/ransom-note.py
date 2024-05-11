// https://leetcode.com/problems/ransom-note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dt = Counter(magazine)
        for i in ransomNote:
            if i not in dt or dt[i] == 0:
                return False
            dt[i] -= 1
        return True
