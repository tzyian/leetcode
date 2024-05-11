// https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix

# from typing import List
# from bisect import bisect_left

'''
def find_first_negative(cmin, cmax, arr: List[int]) -> int:
    left = cmin
    right = cmax
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < 0:
            right = mid
        else:
            left = mid + 1
    return left
'''


def find_first_negative2(cmin, cmax, arr: List[int]) -> int:
    i = bisect_left(arr, True, cmin, cmax, key=lambda mid: not (mid >= 0))
    if i == len(arr):
        return len(arr) - 1
    return i


'''
bisect version adapted from this link.
Note that bisect assumes the key is in the sorted array, 
or else will return a value outside the array index and you will have to check bounds.
https://fanchenbao.medium.com/full-powered-binary-search-with-bisect-in-python-3-10-fb4a76110746
'''


class Solution:
    def __init__(self):
        self.ncols = -1
        self.nrows = -1
        self.count = -1

    def countNegatives(self, grid: List[List[int]]) -> int:
        self.count = 0
        self.nrows = len(grid)
        self.ncols = len(grid[0])
        self.helper(grid, 0, self.nrows - 1, 0, self.ncols - 1)
        return self.count

    def helper(self, grid, rmin, rmax, cmin, cmax):
        if rmin > rmax or cmin > cmax or rmin < 0 or rmax >= self.nrows or cmin < 0 or cmax >= self.ncols:
            return
        rmid = rmin + (rmax - rmin) // 2
        firstneg = find_first_negative2(cmin, cmax, grid[rmid])
        if grid[rmid][firstneg] >= 0:
            return self.helper(grid, rmid + 1, rmax, cmin, cmax)
        else:
            dc = cmax - firstneg + 1
            dr = rmax - rmid + 1
            self.count += dc * dr
            # top right
            self.helper(grid, rmin, rmid - 1, firstneg, cmax)
            # bottom left
            self.helper(grid, rmid + 1, rmax, cmin, firstneg - 1)
            return


'''
grid = [
    [4, 3, 2, -1],
    [3, 2, 1, -1],
    [1, 1, -1, -2],
    [-1, -1, -2, -3]]
ans = Solution().countNegatives(grid)


arr = [-1, -1, -2, -3, -5]
a = find_first_negative(0, len(arr) - 1, arr)
b = find_first_negative2(0, len(arr) - 1, arr)
print(a == b)
'''