from typing import List


# @leet start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        visited = [False] * n

        def dfs(curr: list[int], visited: list[bool]) -> None:
            if len(curr) == n:
                ans.append(curr[:])
            for i in range(n):
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                if visited[i]:
                    continue
                curr.append(nums[i])
                visited[i] = True
                dfs(curr, visited)
                curr.pop()
                visited[i] = False

        dfs([], visited)
        return ans


# @leet end

x = 0
nums = [1, 1, 2]
x = Solution().permuteUnique(nums)
print(x)

nums = [1, 2, 3]
x = Solution().permuteUnique(nums)
print(x)

