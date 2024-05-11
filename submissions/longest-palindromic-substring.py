// https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start_idx = 0
        end_idx = 0
        for i in range(n):
            # odd
            # 0123456
            for j in range(1, min(i+1, n-i)):
                if s[i-j] != s[i+j]:
                    break
                if 2*j+1 > end_idx - start_idx + 1:
                    start_idx = i-j
                    end_idx = i+j

            # even
            if i + 1 <= n - 1 and s[i+1] == s[i]:
                if 2 > end_idx - start_idx + 1:
                    start_idx = i
                    end_idx = i+1
                for j in range(1, min(i+1, n-i-1)):
                    if s[i-j] != s[i+1+j]:
                        break

                    if 2*j+2 > end_idx - start_idx + 1:
                        start_idx = i-j
                        end_idx = i+1+j
        return s[start_idx:end_idx+1]



        