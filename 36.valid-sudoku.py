# @leet start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        BOARD_SIZE = 9
        for i in range(BOARD_SIZE):
            row_map = set()
            col_map = set()
            for j in range(BOARD_SIZE):
                if board[i][j] == ".":
                    pass
                elif board[i][j] in row_map:
                    return False
                else:
                    row_map.add(board[i][j])

                if board[j][i] == ".":
                    pass
                elif board[j][i] in col_map:
                    return False
                else:
                    col_map.add(board[j][i])

        NUM_SUB = 3
        SUB_SIZE = 3
        for a in range(NUM_SUB):
            for b in range(NUM_SUB):
                cell_map = set()
                for i in range(SUB_SIZE):
                    for j in range(SUB_SIZE):
                        r = a * SUB_SIZE + i
                        c = b * SUB_SIZE + j
                        if board[r][c] == ".":
                            continue

                        if board[r][c] in cell_map:
                            return False
                        cell_map.add(board[r][c])
        return True


# @leet end

test = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

Solution().isValidSudoku(test)
