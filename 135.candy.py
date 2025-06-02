from typing import List


# @leet start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        # O(n) TC
        # O(n) SC for the return

        # each child must have one candy
        # higher rating than neighbour  -> more candy (P -> Q)
        # more candy -/> higher rating than neighbour (Q -/> P)
        n = len(ratings)
        candy = [1] * n
        # forward
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1

        # backward
        for j in range(n - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                candy[j] = max(candy[j + 1] + 1, candy[j])
        return sum(candy)

        # # ok working with separation partitions of mins and min-1/min+1 wont work either
        # # ok the below wont work cos when you set a candy to 1, the min could have actually be 1 i.e. set it to -1 before adding
        # mn = min(candy)
        # tot = sum(candy)
        # if mn < 1:
        #     tot += n * (1 - mn)
        #
        # return tot


# @leet end

r = [1, 2, 2]
r = [1, 10, 100, 99, 98, 2, 1, 95]
x = Solution().candy(r)
print(x)

