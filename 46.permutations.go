package leetcode

// @leet start
func permute(nums []int) [][]int {
	n := len(nums)
	ans := [][]int{}
	visited := make([]bool, n)
	curr := []int{}
	backtrack(&nums, &ans, &curr, &visited)

	return ans
}

func backtrack(nums *[]int, ans *[][]int, curr *[]int, visited *[]bool) {
	if len(*curr) == len(*visited) {
		currCopy := make([]int, len(*curr))
		copy(currCopy, *curr)
		*ans = append(*ans, currCopy)
		return
	}

	for i := range len(*nums) {
		if !(*visited)[i] {
			*curr = append(*curr, (*nums)[i])
			(*visited)[i] = true
			backtrack(nums, ans, curr, visited)
			(*visited)[i] = false
			*curr = (*curr)[:len(*curr)-1]
		}

	}

}

// @leet end

