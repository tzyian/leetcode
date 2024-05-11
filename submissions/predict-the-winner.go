// https://leetcode.com/problems/predict-the-winner

import (
	"fmt"
)

const (
	P1 int = 1
	P2     = -1
)

// dp over the difference in score.
// if >= 0, player 1 has more points (p1 wins if diff is 0)
// if <0, player 2 has more points

func PredictTheWinner(nums []int) bool {
	n := len(nums)
	dp := make(map[int]map[int]int, n)
	p1HigherScore := helper(nums, dp, 0, n-1, P1)
	return p1HigherScore >= 0
}

/*
start\end
       0 1 2  3
    0     <-- *
    1         |
    2         v
    3
*/

func helper(nums []int, dp map[int]map[int]int, start int, end int, player int) int {
	n := len(nums)
	if (start < 0 || end >= n) && player == P1 {
		return -(2 << 30) // P1 wants to max, so default to -inf
	} else if (start < 0 || end >= n) && player == P2 {
		return 2 << 30 // P2 wants to min, so default to inf
	} else if start == end {
		// no need to check further
		if player == P1 {
			return nums[start]
		} else {
			return -nums[start]
		}
	}

	// check if already memoized
	if _, ok := dp[start]; ok {
		if val, ok := dp[start][end]; ok {
			return val
		}
	} else {
		dp[start] = make(map[int]int)
	}

	// If p1 (player = 1), then add to diff. If p2 (player = -1), subtract from diff.
	startVal := nums[start] * player
	endVal := nums[end] * player

	takeStart := startVal + helper(nums, dp, start+1, end, -player)
	takeEnd := endVal + helper(nums, dp, start, end-1, -player)

	var result int
	if player == P1 {
		result = max(takeStart, takeEnd)
	} else {
		result = min(takeStart, takeEnd)
	}
	dp[start][end] = result
	return result

}

// Helper function to return the maximum of two integers.
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// Helper function to return the minimum of two integers.
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}