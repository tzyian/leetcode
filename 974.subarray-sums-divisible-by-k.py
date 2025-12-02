# @leet imports start
from typing import List, Optional

# @leet imports end

from collections import defaultdict


# @leet start
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        ans = 0
        psum = 0
        for x in nums:
            psum += x
            ans += counts[psum % k]
            counts[psum % k] += 1

        return ans


# @leet end

n = [4, 5, 0, -2, -3, 1]
k = 5
x = Solution().subarraysDivByK(n, k)
print(x)

s = [4, 9, 9, 7, 4, 5]
m = [4, 4, 4, 2, 4, 0]
a = [0, 1, 2, 0, 3, 0]

