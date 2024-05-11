// https://leetcode.com/problems/relative-ranks

import (
	"sort"
	"strconv"
)

func findRelativeRanks(score []int) []string {
	copied := make([]int, len(score))
	copy(copied, score)
	sort.Slice(copied, func(i, j int) bool {
		return copied[i] > copied[j]
	})

	ranks := make(map[int]string)
	for i, val := range copied {
		if i == 0 {
			ranks[val] = "Gold Medal"
		} else if i == 1 {
			ranks[val] = "Silver Medal"
		} else if i == 2 {
			ranks[val] = "Bronze Medal"
		} else {
			ranks[val] = strconv.Itoa(i + 1)
		}
	}

	ret := make([]string, len(score))
	for i := 0; i < len(score); i++ {
		ret[i] = ranks[score[i]]
	}
	return ret
}
