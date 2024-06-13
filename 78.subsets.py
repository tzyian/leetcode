# @leet start


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        ans = []

        def backtrack(first: int, curr: list[int]):
            ans.append(curr[:])

            for i in range(first, n):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()

        backtrack(0, [])

        return ans


# @leet end
