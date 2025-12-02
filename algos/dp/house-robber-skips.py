from collections import Counter
from typing import List

# House Robber, but constraints are much larger
# to prevent iterating over all values in range
# If you take i, you must skip i+1 and i+2
# Similar to buy and sell tickets


def maximumTotalDamage(power: List[int]) -> int:
    c = Counter(power)

    spells = [0, 0, 0] + sorted(c.keys())
    n = len(spells)
    dp = [0] * n

    for i in range(3, n):
        to_add = spells[i] * c[spells[i]]
        if spells[i] - spells[i - 1] > 2:
            # just take the last spell
            dp[i] = dp[i - 1] + to_add
        elif spells[i] - spells[i - 2] > 2:
            # we have to avoid the previous spell
            dp[i] = max(dp[i - 1], dp[i - 2] + to_add)
        else:
            # this is dp, so we only need to check dp[i-1]
            dp[i] = max(dp[i - 1], dp[i - 3] + to_add)
    return dp[-1]


def rob(nums: List[int]) -> int:
    take = 0
    notake = 0

    n = len(nums)
    for i in range(n):
        temp = take
        take = notake + nums[i]
        notake = max(temp, notake)
    return max(take, notake)
