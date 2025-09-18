# @leet imports start
from typing import *

# @leet imports end
from math import gcd, lcm

# NOTE: you are expected to know greedy works
# i.e. the question will not state the clause
# that any arbitrary order works


# @leet start
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for x in nums:
            stack.append(x)
            while len(stack) >= 2 and gcd(stack[-2], stack[-1]) > 1:
                x1 = stack.pop()
                x2 = stack.pop()
                m = lcm(x1, x2)
                stack.append(m)
        return stack


# @leet end

x = [6, 4, 3, 2, 7, 6, 2]
x = Solution().replaceNonCoprimes(x)
print(x)

[2, 2, 1, 1, 3, 3, 3]

