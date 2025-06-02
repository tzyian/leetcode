from typing import List


# @leet start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # (g-c)
        # key insight: if A -/> C, then any B -/> C

        n = len(gas)
        net = 0
        excess = 0

        start = 0

        for i in range(n):
            diff = gas[i] - cost[i]
            net += diff
            excess += diff
            if excess < 0:
                excess = 0
                start = i + 1

        if net < 0:
            return -1
        return start


# @leet end

g = [1, 2, 3, 4, 5]
c = [3, 4, 5, 1, 2]
x = Solution().canCompleteCircuit(g, c)
print(x)

