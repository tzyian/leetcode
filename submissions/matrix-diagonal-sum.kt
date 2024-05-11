// https://leetcode.com/problems/matrix-diagonal-sum

class Solution {
    fun diagonalSum(mat: Array<IntArray>): Int {
        var len: Int = mat.size
        var sum: Int = 0
        for (i in 0 until len) {
            sum += mat[i][i]
            if (i == len - 1 - i) {
                continue
            }
            sum += mat[i][len - 1 - i]
        }
        return sum
    }
}