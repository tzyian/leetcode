from typing import List


# @leet start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        candidates.sort()
        visited = [False] * n

        def dfs(start: int, curr: list[int], tot: int, visited: list[bool]) -> None:
            if tot == target:
                ans.append(curr[:])

            for i in range(start, n):
                if i > 0 and candidates[i] == candidates[i - 1] and not visited[i - 1]:
                    continue

                if visited[i]:
                    continue

                x = candidates[i]
                if tot + x > target:
                    return

                curr.append(x)
                visited[i] = True
                dfs(i + 1, curr, tot + x, visited)
                curr.pop()
                visited[i] = False

        dfs(0, [], 0, visited)
        return ans


# @leet end

c = [10, 1, 2, 7, 6, 1, 5]
t = 8
x = Solution().combinationSum2(c, t)
print(x)

[2, 5, 2, 1, 2]
5

