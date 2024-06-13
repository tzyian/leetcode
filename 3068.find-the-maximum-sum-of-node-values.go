package local

// @leet start

import (
	"math"
)

func maximumValueSum(nums []int, k int, edges [][]int) int64 {
	// O(n) TC, O(1) SC
	// In any binary tree, you can XOR any two nodes regardless of their position
	// Since a^b^b = a, you can bubble any XOR to the location you want
	// However because of the "edges" constraint (have to XOR both nodes in an edge),
	// it has to be an even number of XORs.

	minDiff := math.MaxInt
	sum := 0
	count := 0

	for _, ele := range nums {
		after := ele ^ k
		diff := after - ele

		if abs(diff) < minDiff {
			minDiff = abs(diff)
		}

		if after > ele {
			count = (count + 1) % 2
			sum += after
		} else {
			sum += ele
		}
	}

	if count == 0 {
		return int64(sum)
	}
	return int64(sum - minDiff)

}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

// @leet end

