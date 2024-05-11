// https://leetcode.com/problems/minimum-cost-to-make-array-equal

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        n = len(nums)
        zipped = zip(nums, cost)
        zipped = sorted(zipped, key=lambda x: x[0])

        def getCost(val: int) -> int:
            total = 0
            for p in zipped:
                total += p[1] * abs(val - p[0])
            return total

        l = zipped[0][0]
        h = zipped[-1][0]
        ans = getCost(nums[0])

        while l < h:
            m = l + (h - l) // 2
            c1 = getCost(m)
            c2 = getCost(m + 1)
            ans = min(c1, c2)

            if c1 > c2:
                l = m + 1
            else: # c1 < c2
                h = m

        return ans