// https://leetcode.com/problems/search-a-2d-matrix

class Solution {
    fun searchMatrix(matrix: Array<IntArray>, target: Int): Boolean {
        return searchMatrix2(matrix, target, 0, matrix.size - 1)
    }


    fun searchMatrix2(matrix: Array<IntArray>, target: Int, 
    up: Int, down: Int): Boolean {
        var midRow = up + (down - up) / 2
        var endCol = matrix[0].size
        if (up > down) {
            return false
        }
        if (matrix[midRow][0] <= target && target <= matrix[midRow][endCol - 1]) {
            return Arrays.binarySearch(matrix[midRow], target) >= 0
        } else if (matrix[midRow][0] < target) {
            return searchMatrix2(matrix, target, midRow + 1, down)
        } else {
            return searchMatrix2(matrix, target, up, midRow - 1)
        }        
    }

    
}