from typing import List


# 309. Buy and Sell Stock with Cooldown


def maxProfit(prices: List[int]) -> int:
    buy = -(10**9)  # none --buy--> *own
    sell = -(10**9)  # own --sell--> *sold
    cd = 0  # sell --wait--> *cooldown

    for p in prices:
        icd = cd
        isell = sell
        ibuy = buy

        buy = max(ibuy, icd - p)
        sell = ibuy + p
        cd = max(isell, icd)
    return max(sell, cd)
