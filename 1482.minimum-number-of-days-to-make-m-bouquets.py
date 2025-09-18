from typing import List


# @leet start
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def condition(day: int) -> bool:
            # check in linear time to see if condition is satisfied
            # i.e. m instances of k consecutive flowers
            formed = 0
            consec = 0
            for e in bloomDay:
                if day >= e:
                    consec += 1
                else:
                    consec = 0

                if consec == k:
                    consec = 0
                    formed += 1
            return formed >= m

        last = max(bloomDay)
        lo = min(bloomDay)
        hi = last
        while lo < hi:
            mid = (lo + hi) // 2
            if condition(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo  # if lo <= last else -1


# @leet end
arr = [7, 7, 7, 7]
m = 2
k = 2
print(Solution().minDays(arr, m, k))  # expect 7

arr = [7, 7, 7, 7]
m = 2
k = 2
print(Solution().minDays(arr, m, k))  # expect 7


arr = [1, 10, 3, 10, 2]
m = 3
k = 1
print(Solution().minDays(arr, m, k))  # expect 3
arr = [1, 10, 3, 10, 2]
m = 3
k = 2
print(Solution().minDays(arr, m, k))  # expect -1
arr = [7, 7, 7, 7, 12, 7, 7]
m = 2
k = 3
print(Solution().minDays(arr, m, k))  # expect 12
arr = [1000000000, 1000000000]
m = 1
k = 1
print(Solution().minDays(arr, m, k))  # expect 100000000
arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
m = 4
k = 2
print(Solution().minDays(arr, m, k))  # expect 9
arr = [5, 7, 7, 7, 7, 7, 7]
m = 3
k = 2
print(Solution().minDays(arr, m, k))  # expect 7
