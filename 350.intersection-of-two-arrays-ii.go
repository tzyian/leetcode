package leetcode

// @leet start
func intersect(nums1 []int, nums2 []int) []int {
	dict := make(map[int]int)
	for _, ele := range nums1 {
		dict[ele]++
	}

	arr := make([]int, 0)

	for _, ele := range nums2 {
		if dict[ele] > 0 {
			arr = append(arr, ele)
			dict[ele]--
		} else {
			delete(dict, ele)
		}
	}

	return arr
}

// @leet end
