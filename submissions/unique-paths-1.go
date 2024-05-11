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

	curr := 1
	for i := 1; i <= k; i++ {
		curr = curr * (n - i + 1) / i
	}

	return curr
}