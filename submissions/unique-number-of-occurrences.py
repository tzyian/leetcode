// https://leetcode.com/problems/unique-number-of-occurrences

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        counts = set()
        for _, v in c.items():
            if v in counts:
                return False
            counts.add(v)

        return True
        