// https://leetcode.com/problems/first-unique-character-in-a-string

class Solution:
    from collections import Counter
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        d = {x : count for x, count in c.items() if count == 1}
        print(f"d and {d}")
        if len(d) == 0:
                return -1
        temp = []
        for i in d.keys():
                temp += [s.index(i)]
        print(min(temp))
        return min(temp)

        
        
        