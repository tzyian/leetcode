// https://leetcode.com/problems/longest-palindromic-subsequence

func longestPalindromeSubseq(s string) int {
    sRev := reverse(s)
    n := len(s)
    dp := make([][]int, n+1)

    for i := range dp {
        dp[i] = make([]int, n+1)
    }

    for i := 1; i < n+1; i++ {
        for j := 1; j < n+1; j++ {
            if s[i-1] == sRev[j-1] {
                dp[i][j] = 1 + dp[i-1][j-1]
            } else {
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            }
        }
    }
    return dp[n][n]
}

func max(a, b int) int {
    if a < b {
        return b
    }
    return a
}


func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}