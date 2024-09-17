package leetcode

// @leet start
// This question specifically doesn't require backtracking, just greedy
// Because any non-negative, can be duplicates

func restoreMatrix(rowSum []int, colSum []int) [][]int {
	numRows := len(rowSum)
	numCols := len(colSum)

	mat := make([][]int, numRows)
	for i := range numRows {
		mat[i] = make([]int, numCols)
	}

	r := 0
	c := 0

	for r < numRows && c < numCols {
		minVar := min(rowSum[r], colSum[c])
		mat[r][c] = minVar

		rowSum[r] -= minVar
		colSum[c] -= minVar

		if rowSum[r] == 0 {
			r++
		} else {
			c++
		}

	}

	return mat

}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// @leet end
