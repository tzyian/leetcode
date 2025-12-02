# @leet imports start
from typing import List, Optional

# @leet imports end


from bisect import bisect_left, bisect_right


# @leet start
class Solution:
    # NOTE: pure bsearch won't work because there are -ve numbers
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        psums = [nums[0]]
        n = len(nums)
        for i in range(1, n):
            psums.append(psums[i - 1] + nums[i])

        ans = 0
        # for each number in psums, bsearch to find lower range and upper range
        # psums[lower] - psums[i] >= lower
        # psums[upper] - psums[i] <= upper
        # tot += upper - lower + 1

        for i in range(n):
            lower_range = bisect_left(psums, lower, lo=i, hi=n)
            upper_range = bisect_right(psums, upper, lo=i, hi=n)
            ans += upper_range - lower_range + 1

        return ans


# @leet end

n = [-2, 5, -1]
psum = [-2, 3, 2]
l = -2
u = 2
x = Solution().countRangeSum(n, l, u)
print(x)  # expect 3

[0]
0
0

