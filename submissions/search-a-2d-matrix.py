// https://leetcode.com/problems/search-a-2d-matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        grid = matrix
        nRows = len(grid)
        if nRows == 0:
            return False
        nCols = len(grid[0])

        lo = 0
        hi = nRows * nCols - 1 # last element of the grid
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            # find the rowInd and colInd corresponding to mid
            rowInd = mid // nCols # row Index corresponding to mid
            colInd = mid - rowInd * nCols 

            midEle = grid[rowInd][colInd]

            if midEle == target:
                return True
            elif midEle > target: # search left
                hi = mid - 1
            else:
                lo = mid + 1
        return False