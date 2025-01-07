# https://leetcode.com/problems/permutations/
# @leet start
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        def backtrack(curr: list[int], visited: list[bool]):
            if len(curr) == n:
                ans.append(curr.copy())
            else:
                for i in range(n):
                    if not visited[i]:
                        curr.append(nums[i])
                        visited[i] = True
                        backtrack(curr, visited)
                        curr.pop()
                        visited[i] = False

        backtrack([], [False] * n)
        return ans


# @leet end

