from collections import defaultdict
from heapq import heappop, heappush
from typing import List


# @leet start
class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        # Heap can store up to k * n elements
        # So each heappop is log(k*n)
        # There are E * k relaxations
        # TC = k*n log(k*n) + E * k
        # The grid is of size k * n
        # SC = k*n for grid + heap + adjlist

        # construct adj list
        nodes = defaultdict(dict)
        for fr, to, price in flights:
            nodes[fr][to] = price

        k += 1  # change k to depth from src rather than intermediate nodes

        MAX_INT = 10**9  # there are at most n^2 connections and price <= 10**4
        pq = [(0, 0, src)]  # (wt, stops, curr)
        prices = [[MAX_INT] * (k + 1) for _ in range(n)]  # nodes * depth
        prices[src][0] = 0
        min_price = MAX_INT

        while pq:
            p_to_curr, depth, curr = heappop(pq)
            if depth > k:
                continue

            if curr == dst:
                min_price = min(min_price, p_to_curr)

            # you can't do wt < min_wt || depth < min_depth
            # because there can be suitable paths that are
            # not strictly better than either (between)

            for v, edge in nodes[curr].items():
                new_wt = p_to_curr + edge
                if new_wt < prices[v][depth]:
                    prices[v][depth] = new_wt
                    heappush(pq, (new_wt, depth + 1, v))

        return min_price if min_price < MAX_INT else -1


# @leet end

n = 4
f = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
s = 0
d = 3
k = 1

x = Solution().findCheapestPrice(n, f, s, d, k)
print(x)
