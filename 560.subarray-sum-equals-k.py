# @leet imports start
from collections import defaultdict
from typing import List, Optional

# @leet imports end

# @leet start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        psums = defaultdict(int)
        psums[0] = 1
        ans = 0
        psum = 0
        for x in nums:
            psum += x
            ans += psums[psum - k]
            psums[psum] += 1

        return ans


# @leet end

n = [1, 1, 1]
k = 2
x = Solution().subarraySum(n, k)
print(x)

[1, 2, 3]
3

