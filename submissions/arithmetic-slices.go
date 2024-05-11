// https://leetcode.com/problems/arithmetic-slices

func numberOfArithmeticSlices(nums []int) int {
    n := len(nums)
    count := 0
    dp := make([]int, n)
    for i := 2; i < n; i++ {
        if nums[i] - nums[i-1] == nums[i-1] - nums[i-2] {
            dp[i] = dp[i-1] + 1
        }
    }
    for _, ele := range dp {
        count += ele
    }
    return count
}