# @leet start
from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # O(n) time, space
        # See the other file

        n = len(boxes)
        if n <= 1:
            return [0] * n

        balls = [int(i) for i in list(boxes)]

        # don't actually need to keep all the values, just keep in ans array here

        # the number of balls in each box when shifting balls right
        pballs = balls.copy()
        # the number of ops to shift all balls from prev box to this box
        p_ops = [0] * n
        for i in range(1, n):
            p_ops[i] = p_ops[i - 1] + pballs[i - 1]
            pballs[i] += pballs[i - 1]

        sballs = balls.copy()
        s_ops = [0] * n
        for i in range(n - 2, -1, -1):
            s_ops[i] = s_ops[i + 1] + sballs[i + 1]
            sballs[i] += sballs[i + 1]

        ans = [0] * n
        for i in range(n):
            ans[i] = s_ops[i] + p_ops[i]

        return ans


# @leet end

