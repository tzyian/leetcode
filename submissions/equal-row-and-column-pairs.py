// https://leetcode.com/problems/equal-row-and-column-pairs

from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ctr = defaultdict(int)
        n = len(grid)
        
        ctr = Counter(tuple(row) for row in grid)
        
        ans = 0
        for i in range(n):
            c = []
            for j in range(n):
                c.append(grid[j][i])
            cset = tuple(c)
            if cset in ctr:
                ans += ctr[cset]
        
        return ans
            


        