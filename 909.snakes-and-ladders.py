from collections import deque
from typing import List


# @leet start
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # this is a graph problem
        # first plot the grid number to coordinates
        # then for every square, there are 6 neighbours
        # then do bfs

        n = len(board)
        total = n * n

        def get_coords(x: int) -> tuple[int, int]:
            x -= 1
            from_bottom = x // n
            row = n - 1 - from_bottom
            col = x % n  # go right

            if from_bottom & 1 == 1:
                # go left
                col = n - 1 - col

            return (row, col)

        ROLL_START = 1
        ROLL_STOP = 6

        # bfs
        start = 1

        queue = deque([start])
        visited = [False] * (total + 1)
        visited[start] = True
        count = 0

        while queue:
            ql = len(queue)
            for _ in range(ql):
                curr = queue.popleft()
                if curr == total:
                    return count

                deepest_plain = -1

                for roll in range(ROLL_START, ROLL_STOP + 1):
                    if curr + roll > total:
                        break
                    ni, nj = get_coords(curr + roll)
                    label = board[ni][nj]
                    if label == -1:
                        deepest_plain = curr + roll
                    else:
                        if not visited[label]:
                            visited[label] = True
                            queue.append(label)

                if deepest_plain != -1 and not visited[deepest_plain]:
                    queue.append(deepest_plain)
                    visited[deepest_plain] = True

            count += 1

        return -1


# @leet end


board = [
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 35, -1, -1, 13, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 15, -1, -1, -1, -1],
]
board = [
    [-1, 1, 2, -1],
    [2, 13, 15, -1],
    [-1, 10, -1, -1],
    [-1, 6, 2, 8],
]  # exp 2
x = Solution().snakesAndLadders(board)
print(x)

