// https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        numstring = str(x)
        for i in range(len(numstring)//2):
            if numstring[i] != numstring[-(i+1)]:
                print(numstring[i])
                return False
        return True