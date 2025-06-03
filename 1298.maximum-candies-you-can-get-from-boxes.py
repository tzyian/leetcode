from collections import deque
from typing import List


# @leet start
class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int],
    ) -> int:

        n = len(status)
        owned_boxes = deque(initialBoxes)
        owned_keys = [False] * n
        UNLOCKED = 1
        LOCKED = 0
        visited = [False] * n
        # NOTE: visited array here is only used to note which boxes that need to be rechecked
        # so each box is only checked at most twice
        ans = 0

        while owned_boxes:
            b = owned_boxes.pop()
            if status[b] == UNLOCKED or (status[b] == LOCKED and owned_keys[b]):
                status[b] = UNLOCKED
                for k in keys[b]:
                    owned_keys[k] = True
                for nb in containedBoxes[b]:
                    owned_boxes.append(nb)
                ans += candies[b]
            elif not visited[b]:
                visited[b] = True
                owned_boxes.appendleft(b)

        return ans


# @leet end

s = [1,0,1,0]
c = [7,5,4,100]
k = [[],[],[1],[]]
cb = [[1,2],[3],[],[]]
ib = [0]
x = Solution().maxCandies(s,c,k,cb,ib)
print(x)

