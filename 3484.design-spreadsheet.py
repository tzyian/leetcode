# @leet imports start
from collections import defaultdict
from typing import *

# @leet imports end


# @leet start
class Spreadsheet:

    def __init__(self, rows: int):
        self.d = [dict() for _ in range(26)]

    def getCellIndices(self, cell: str) -> Tuple[int, int]:
        r, c = int(cell[1:]) - 1, ord(cell[0]) - ord("A")
        return r, c

    def setCell(self, cell: str, value: int) -> None:
        r, c = self.getCellIndices(cell)
        self.d[c][r] = value

    def resetCell(self, cell: str) -> None:
        r, c = self.getCellIndices(cell)
        if r in self.d[c]:
            del self.d[c][r]

    def getValue(self, formula: str) -> int:
        def parse(x: str) -> int:
            if x[0].isalpha():
                r, c = self.getCellIndices(x)
                return self.d[c].get(r, 0)
            return int(x)

        x, y = formula[1:].split("+")
        return parse(x) + parse(y)


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
# @leet end

