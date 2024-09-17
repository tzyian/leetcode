# @leet start
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # copied from https://leetcode.com/problems/maximum-product-subarray/solutions/183483/java-c-python-it-can-be-more-simple/
        # best must include either first or last element or both
        # so multiplying all the way to get the maximum
        ans = nums[0]
        prefix = nums
        suffix = prefix[::-1]
        for i in range(1, len(nums)):
            prefix[i] *= prefix[i - 1] or 1  # prefix sum
            suffix[i] *= suffix[i - 1] or 1  # suffix sum
            # include `or 1` in case of 0's where
            # you drop the preceding subarray and start anew
            ans = max(ans, prefix[i], suffix[i])
        return ans

    def maxProductKadane(self, nums: List[int]) -> int:
        minp = 1
        maxp = 1
        best = -float("inf")
        for ele in nums:
            ominp = min(maxp * ele, minp * ele, ele)
            omaxp = max(maxp * ele, minp * ele, ele)
            minp = ominp
            maxp = omaxp

            best = max(best, maxp)

        return best

    def maxProductKadaneVerbose(self, nums: List[int]) -> int:
        minp = 1
        maxp = 1
        best = -float("inf")
        for ele in nums:
            if ele < 0:
                ominp = min(maxp * ele, ele)
                omaxp = max(minp * ele, ele)

                minp = ominp
                maxp = omaxp
            else:
                omaxp = max(maxp * ele, ele)
                ominp = min(minp * ele, ele)

                maxp = omaxp
                minp = ominp
            best = max(best, maxp)
            print(minp, maxp, best)

        return best


# @leet end

n0 = [2, 3, -2, 4]
n1 = [-2, 0, -1]
n2 = [-1, -2, -9, -6]
x = Solution().maxProduct(n2)
print(x)
