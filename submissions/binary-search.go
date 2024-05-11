// https://leetcode.com/problems/binary-search

func search(nums []int, target int) int {
    n := len(nums)
    l, h := 0, n - 1

    for l < h {
        m := l + (h - l) / 2
        if nums[m] >= target {
            h = m
        } else {
            l = m + 1
        }
    }
    
    if nums[l] == target {
        return l
    }
    return -1
}