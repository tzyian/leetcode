// https://leetcode.com/problems/powx-n

from functools import cache

def helper(x: float, n: int) -> float:
    if x == 0:
        return 0
    elif n == 0:
        return 1
    elif n < 0:
        x = 1/x
        n = -n

    curr_pow = 1
    curr = x

    while curr_pow * 2 < n:
        curr = curr * curr
        curr_pow = curr_pow * 2
    diff = n - curr_pow
    return curr * helper(x, diff)


class Solution:
    def myPow(self, x: float, n: int) -> float:
        return helper(x, n)

        
        
