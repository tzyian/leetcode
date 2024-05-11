// https://leetcode.com/problems/boats-to-save-people


import (
	"slices"
)

func numRescueBoats(people []int, limit int) int {
	slices.Sort(people)

	n := len(people)
	left, right := 0, n-1
	count := 0

	for left <= right {
		if (people[left] + people[right]) > limit {
			right--
		} else {
			left++
			right--
		}
		count++
	}
	return count
}
