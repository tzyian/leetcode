# @leet start
from typing import List

import numpy as np


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        mat = np.array(matrix)
        row_min_vals = np.min(mat, axis=1)
        col_max_vals = np.max(mat, axis=0)
        is_lucky = np.isin(row_min_vals, col_max_vals)
        return row_min_vals[is_lucky].tolist()


# @leet end
