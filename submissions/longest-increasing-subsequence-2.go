// https://leetcode.com/problems/longest-increasing-subsequence

// alternatively, dont set dp[i] = 1 and instead,
// maxSubseq := 0 and add 1 to answer

func lengthOfLIS(nums []int) int {
    // O(n^2) TC
    // O(n) SC
    n := len(nums)
    dp := make([]int, n)
    maxSubseq := 1

    for i, ele := range nums {
        dp[i] = 1
        for j := 0; j < i; j++ {
            // ele > nums[j] because must be increasing
            // dp[i] < dp[j] + 1 because take the max subseq ele j
            if (ele > nums[j]) && (dp[i] < dp[j] + 1) {
                dp[i] = dp[j] + 1

                if dp[i] > maxSubseq {
                    maxSubseq = dp[i]
                }

            }
        }
    }
    return maxSubseq
}