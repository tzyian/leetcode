// https://leetcode.com/problems/first-bad-version

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


# isBadVersion is 1-indexed

def isBad(x):
    return isBadVersion(x + 1)

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1 or isBad(0) == True:
            return 1

        l = 0
        h = n - 1
        mid = l + (h - l) // 2
        while l < h:
            mid = l + (h - l) // 2
            if isBad(mid) and not isBad(mid - 1):
                return mid + 1
            elif isBad(mid):
                h = mid
            else:
                l = mid + 1
        return h + 1