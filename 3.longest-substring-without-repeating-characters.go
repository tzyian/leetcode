package leetcode

// @leet start
func lengthOfLongestSubstring(s string) int {
	l := 0
	r := 0
	n := len(s)
	maxLength := 0
	lastIndex := make(map[byte]int)

	for r < n {
		c := s[r]
		idx, ok := lastIndex[c]

		if ok && idx >= l {
			l = idx + 1
		}
		lastIndex[c] = r

		maxLength = max(r-l+1, maxLength)
		r++
	}

	return maxLength

}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// @leet end

