# @leet imports start
from collections import defaultdict, deque
from typing import List, Optional

# @leet imports end


# @leet start
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        nbs = defaultdict(list)
        for i, x in enumerate(arr):
            nbs[x].append(i)

        queue = deque([0])
        visited = set()
        steps = 0

        def process(idx: int):
            if 0 <= idx < n and idx not in visited:
                visited.add(idx)
                queue.append(idx)

        while queue:
            m = len(queue)
            for _ in range(m):
                curr = queue.popleft()
                if curr == n - 1:
                    return steps

                nbsx = nbs[arr[curr]]
                if nbsx:
                    process(nbsx.pop())
                process(curr + 1)
                process(curr - 1)
                while nbsx:
                    process(nbsx.pop())
                nbsx.clear()
            steps += 1

        return steps


# @leet end

