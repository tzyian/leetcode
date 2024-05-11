// https://leetcode.com/problems/unique-paths

import "fmt"

func uniquePaths(m int, n int) int {
	return binomCoeff(m+n-2, min(n-1, m-1))
}

func min(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

// nCk = n-1 C k-1 + n-1 C k

func binomCoeff(n int, k int) int {
	if n < k {
		panic("n < k")
	}
	grid := make([][]int, n+1)
	for j := range grid {
		grid[j] = make([]int, k+1)
	}

	for i := 0; i < n+1; i++ {
		for j := 0; j < k+1; j++ {
			if i < j {
				break
			} else if j == 0 {
				grid[i][j] = 1
			} else {
				grid[i][j] = grid[i-1][j-1] + grid[i-1][j]
			}

		}
	}
	return grid[n][k]
}
