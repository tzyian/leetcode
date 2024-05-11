// https://leetcode.com/problems/longest-common-subsequence

from functools import cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        @cache
        def helper(i: int, j: int) -> int:
            if i == n or j == m:
                return 0

            if text1[i] == text2[j]:
                return 1 + helper(i+1, j+1)
            
            return max(helper(i+1, j), helper(i, j+1))

        
        return helper(0, 0)

    
        