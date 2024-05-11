// https://leetcode.com/problems/minimum-falling-path-sum

from functools import cache
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        
        @cache
        def helper(i: int, j: int) -> int:
            if i < 0 or i >= n or j < 0 or j >= m:
                return 1e9
            elif i == n - 1:
                return matrix[i][j]
            else:
                return matrix[i][j] + min(
                    helper(i+1,j-1),
                    helper(i+1,j),
                    helper(i+1,j+1)
                )
                
        
        return min(helper(0, j) for j in range(m))
        
        
        