# @leet imports start
from collections import deque
from typing import List

# @leet imports end


# @leet start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        edges = deque()
        visited = set()

        for i in range(n):
            if board[i][0] == "O":
                edges.append((i, 0))
            if board[i][m - 1] == "O":
                edges.append((i, m - 1))

        for j in range(m):
            if board[0][j] == "O":
                edges.append((0, j))
            if board[n - 1][j] == "O":
                edges.append((n - 1, j))

        def leave_xes(i, j) -> bool:
            return (
                0 <= i < n
                and 0 <= j < m
                and board[i][j] == "O"
                and (i, j) not in visited
            )

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while edges:
            i, j = edges.popleft()
            visited.add((i, j))
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if leave_xes(ni, nj):
                    edges.append((ni, nj))
                    visited.add((ni, nj))

        for i in range(n):
            for j in range(m):
                if (i, j) not in visited:
                    board[i][j] = "X"


# @leet end

board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"],
]
x = Solution().solve(board)
print(board)

