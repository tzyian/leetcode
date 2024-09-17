# @leet start
from typing import List

Coord = tuple[int, int]


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        dirs = [0, 1, 0, -1, 0]
        self.found = False

        def dfs(curr: Coord, idx: int, visited: set[Coord]) -> None:
            if idx == len(word):
                self.found = True
                return

            visited.add(curr)

            for i in range(1, len(dirs)):
                dr, dc = dirs[i - 1], dirs[i]
                r, c = curr
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < n
                    and 0 <= nc < m
                    and (nr, nc) not in visited
                    and board[nr][nc] == word[idx]
                ):
                    dfs((nr, nc), idx + 1, visited)
                if self.found:
                    return

            visited.remove(curr)

        for i, row in enumerate(board):
            for j, ele in enumerate(row):
                if ele == word[0]:
                    dfs((i, j), 1, set())
                    if self.found:
                        return True
        return False


# @leet end
