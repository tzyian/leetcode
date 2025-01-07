# @leet start
from functools import cache
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        one, sev, thirt = costs
        n = len(days)

        @cache
        def rec(day_ind: int) -> int:
            if day_ind == n:
                return 0
            a = one + rec(day_ind + 1)

            i = day_ind

            while i < n and days[i] < days[day_ind] + 7:
                i += 1
            b = sev + rec(i)

            while i < n and days[i] < days[day_ind] + 30:
                i += 1
            c = thirt + rec(i)

            return min(a, b, c)

        return rec(0)


# @leet end

