// https://leetcode.com/problems/rotate-image

class Solution {
    fun rotate(matrix: Array<IntArray>): Unit {
        // Transpose
        for (i in matrix.indices) {
            for (j in i + 1 until matrix[0].size) {
                val temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
            }
        }

        // Swap LTR
        for (i in matrix.indices) {
            for (j in 0 until matrix.size / 2) {
                val temp = matrix[i][j]
                matrix[i][j] = matrix[i][matrix.size - 1 - j]
                matrix[i][matrix.size - 1 - j] = temp
            }
        }
    }
}