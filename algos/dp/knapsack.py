# find 2 partitions that minimise the difference between the 2 sums
# see 1049.last-stone-weight.py


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # iterate through all possible sums of combinations of + and -
        dp = set()
        dp.add(0)
        for wt in stones:
            new_dp = set()
            for st in dp:
                # for every existing sum,
                # include sum+wt and sum-wt
                new_dp.add(st + wt)
                new_dp.add(st - wt)
            dp = new_dp
        return min(abs(i) for i in dp)
