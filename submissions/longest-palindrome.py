// https://leetcode.com/problems/longest-palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = Counter(s)
        # a palindrome must have all even + 1 odd
        length = 0
        oddexist = False
        for i in d:
            if d[i] % 2 == 1: 
                oddexist = True
                length += d[i] - 1
            else:
                length += d[i]
        if oddexist:
            length += 1
        return length