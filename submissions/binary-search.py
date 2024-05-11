// https://leetcode.com/problems/binary-search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def bin(start, end):
            if start > end:
                return -1
            mid = start + (end - start) // 2
            print(mid)
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                return bin(start, mid - 1)
            else:
                return bin(mid + 1, end)

        return bin(0, n - 1)


        