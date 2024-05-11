// https://leetcode.com/problems/spiral-matrix-ii

class Solution {
    fun generateMatrix(n: Int): Array<IntArray> {
        val array = Array(n){ IntArray(n) }
        var row = 0
        var col = 0
        var direction = 0
        var size = n

        for (i in 1..n * n) {
            when (direction) {
                0 -> { // right
                    if (col == size - 1) {
                        direction++
                        array[row++][col] = i
                    } else {
                        array[row][col++] = i
                    }
                }
                1 -> { // down
                    if (row == size - 1) {
                        size--
                        direction++
                        array[row][col--] = i
                    } else {
                        array[row++][col] = i
                    }
                }
                2 -> { // left
                    if (col == n - 1 - size) {
                        direction++
                        array[row--][col] = i
                    } else {
                        array[row][col--] = i
                    }
                }
                3 -> { // up
                    if (row == n - size) {
                        direction = 0
                        array[row][col++] = i
                    } else {
                        array[row--][col] = i
                    }
                }
                else -> throw Exception("Invalid direction")
            }
        }
        return array
    }
}