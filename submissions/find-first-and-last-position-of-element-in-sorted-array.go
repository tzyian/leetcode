// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

func searchRange(nums []int, target int) []int {
    return []int{min(nums, target), max(nums, target)}
}

func min(nums []int, target int) int {
    n := len(nums)
    if n == 0 {
        return -1
    }
    h, l := n - 1, 0    
    for l < h {
        m := l + (h - l) / 2
        if nums[m] < target {
            l = m + 1
        } else {
            h = m
        }
    }
    if nums[l] == target {
        return l
    }
    return -1
}


func max(nums []int, target int) int {
    n := len(nums)
    if n == 0 {
        return -1
    }
    h, l := n - 1, 0    
    for l < h {
        m := l + (h - l) / 2 + 1
        if nums[m] <= target {
            l = m
        } else {
            h = m - 1
        }
    }
    if nums[l] == target {
        return l
    }
    return -1
}

