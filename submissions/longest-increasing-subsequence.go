// https://leetcode.com/problems/longest-increasing-subsequence

func lengthOfLIS(nums []int) int {
    n := len(nums)
    dp := make([]int, n)
    maxSubseq := 0

    for i, ele := range nums {
        for j := 0; j < i; j++ {
            if (ele > nums[j]) && (dp[i] < dp[j] + 1) {
                dp[i] = dp[j] + 1

                if dp[i] > maxSubseq {
                    maxSubseq = dp[i]
                }

            }
        }
    }
    return maxSubseq + 1
}