// https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while a or b or c: # no guarantee a or b or c have the same number of bits required in representation
            a2 = a & 1
            b2 = b & 1
            c2 = c & 1
            if c2 == 1 and a2 | b2 != 1:
                count += 1
            elif c2 == 0: # and a2 & b2 != 0: # this condition already accounted for in a2 + b2
                count += a2 + b2


            c >>= 1
            b >>= 1
            a >>= 1
        return count
                
