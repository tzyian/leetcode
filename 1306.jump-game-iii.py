from collections import deque
from typing import List


# @leet start
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # bfs

        goals = set(i for i, v in enumerate(arr) if v == 0)
        if not goals:
            return False

        queue = deque()
        queue.append(start)
        n = len(arr)
        visited = set()
        visited.add(start)

        while queue:
            curr = queue.popleft()

            if curr in goals:
                return True

            add = curr + arr[curr]
            sub = curr - arr[curr]
            if 0 <= add < n and add not in visited:
                queue.append(add)
                visited.add(add)
            if 0 <= sub < n and sub not in visited:
                queue.append(sub)
                visited.add(sub)
        return not goals


# @leet end

a = [4, 2, 3, 0, 3, 1, 2]
s = 5
x = Solution().canReach(a, s)
print(x)

a = [4, 2, 3, 0, 3, 1, 2]
s = 0
x = Solution().canReach(a, s)
print(x)

a = [3, 0, 2, 1, 2]
s = 2
x = Solution().canReach(a, s)
print(x)
