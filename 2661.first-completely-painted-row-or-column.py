# @leet start
from collections import defaultdict
from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        positions = dict()
        num_in_row = defaultdict(int)
        num_in_col = defaultdict(int)
        nrows = len(mat)
        ncols = len(mat[0])

        for i, row in enumerate(mat):
            for j, ele in enumerate(row):
                positions[ele] = (i, j)

        for idx, ele in enumerate(arr):
            i, j = positions[ele]
            num_in_row[i] += 1
            num_in_col[j] += 1
            if num_in_row[i] == ncols or num_in_col[j] == nrows:
                return idx

        raise Exception("Shouldn't reach here")


# @leet end

