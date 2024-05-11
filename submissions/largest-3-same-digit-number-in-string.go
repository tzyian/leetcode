// https://leetcode.com/problems/largest-3-same-digit-number-in-string

import (
	"fmt"
	"strconv"
)

func largestGoodInteger(num string) string {
	var slices []string
	for i := 0; i < len(num)-2; i++ {
		unique := make(map[rune]struct{})
		substr := num[i : i+3]
		for _, j := range substr {
			unique[j] = struct{}{}
		}
		if len(unique) == 1 {
			slices = append(slices, substr)
		}
	}

	maxNum := ""
	for _, num := range slices {
		maxNum = maxString(maxNum, num)
	}
	return maxNum
}

func maxString(a string, b string) string {
	na, _ := strconv.Atoi(a)
	nb, _ := strconv.Atoi(b)
	if na > nb {
		return a
	}
	return b
}
