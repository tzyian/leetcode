package leetcode

// @leet start
func passThePillow(n int, time int) int {
	// for n people, n-1 passes to reach the last person
	// 1 2 3 4 5 6
	// n = 3

	passes := time / (n - 1)

	if passes%2 == 0 {
		return time%(n-1) + 1
	}
	return n - time%(n-1)

}

// @leet end
