// https://leetcode.com/problems/longest-arithmetic-subsequence



func longestArithSeqLength(nums []int) int {
    n := len(nums)
    maxLength := 0
    dp := make([]map[int]int, n)

    for right := 0; right < n; right++ {
        dp[right] = make(map[int]int)
        for left := 0; left < right; left++ {
            diff := nums[left] - nums[right]
            i, ok := dp[left][diff]
            if !ok {
                i = 1
            }
            i++
            dp[right][diff] = i
            if dp[right][diff] > maxLength {
                maxLength = dp[right][diff]
            }
        }
    }
    return maxLength
}