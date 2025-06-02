package leetcode

import "slices"

// @leet start
func permuteUnique(nums []int) [][]int {
	n := len(nums)
	ans := [][]int{}
	curr := []int{}
	visited := make([]bool, n)
	// sort for the line below
	slices.Sort(nums)

	var backtrack func()
	backtrack = func() {
		if len(curr) == len(nums) {
			copied := make([]int, len(curr))
			copy(copied, curr)
			ans = append(ans, copied)
			return
		}

		for i := range nums {
			if visited[i] {
				continue
			}
			// this is the key line difference here to ensure prev elements are visited
			// before the current element if they're the same.
			// This ensures that the prev one can be permuted
			if i > 0 && nums[i-1] == nums[i] && !visited[i-1] {
				continue
			}

			visited[i] = true
			curr = append(curr, nums[i])
			backtrack()
			curr = curr[:len(curr)-1]
			visited[i] = false
		}

	}
	backtrack()

	return ans

}

// @leet end

