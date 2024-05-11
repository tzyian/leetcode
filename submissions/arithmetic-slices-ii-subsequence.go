// https://leetcode.com/problems/arithmetic-slices-ii-subsequence

// note to self: look up length k, or >= k

func numberOfArithmeticSlices(nums []int) int {
    // O(n^2) TC and SC
    n := len(nums)
    ans := 0
    dp := make([]map[int]int, n)

    for i := range nums { // all the numbers
        dp[i] = make(map[int]int)
        for j := 0; j < i; j++ { // all the numbers before that form the subseq
            diff := nums[i] - nums[j]
            // dp[i][diff] is the no of subseq of 2 ele ending with nums[i]
            //      note that 2 ele, because 1 ele cant have a diff
            // dp[j][diff] is the no of subseq of 3 ele ending with nums[i]

            // adding dp[j][diff] here where j is >=2nd ele, and i is >=3rd ele
            // +1 because there is now +1 subseq ending in i which has j
            // i.e. 1 + wishful thinking the no of subseq ending in the previous ele
            // (if not +1, everything will be 0)
            dp[i][diff] += dp[j][diff] + 1
            ans += dp[j][diff]
        }
    }

    return ans
}