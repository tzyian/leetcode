// @leet start
func mostPoints(questions [][]int) int64 {
	n := len(questions)
	dp := make([]int64, n+1)

	for i := n - 1; i >= 0; i-- {
		points := questions[i][0]
		bpow := questions[i][1]
		take := int64(points) + dp[min(i+bpow+1, n)]
		notake := dp[i+1]
		dp[i] = max(take, notake)
	}

	return dp[0]
}

func max(a, b int64) int64 {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// @leet end
