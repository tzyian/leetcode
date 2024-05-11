// https://leetcode.com/problems/search-insert-position

func searchInsert(nums []int, target int) int {
    n := len(nums)
    l := 0
    h := n - 1
    for l < h {
        m := l + (h - l) / 2
        if nums[m] < target {
            l = m +1
        } else {
            h = m
        }
    }
    if target > nums[l] {
        return l + 1
    }
    return l
}