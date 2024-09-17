package leetcode

// @leet start
func minOperations(logs []string) int {
	dist := 0
	for _, str := range logs {
		if str == "../" {
			if dist > 0 {
				dist--
			}
			// else do nothing
		} else if str == "./" {
			// do nothing
		} else {
			dist++
		}

	}
	return dist

}

// @leet end
