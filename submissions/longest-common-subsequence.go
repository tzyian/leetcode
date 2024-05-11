// https://leetcode.com/problems/longest-common-subsequence

func longestCommonSubsequence(text1 string, text2 string) int {
    n := len(text1)
    m := len(text2)
    dp := make([][]int, n+1)

    for i := 0; i < n+1; i++ {
        dp[i] = make([]int, m+1)
    }

    // +1 because comparing subseq before, and at i=j=0, is empty string
    for i := 1; i < n+1; i++ {
        for j := 1; j < m+1; j++ {
            if text1[i-1] == text2[j-1] {
                dp[i][j] = 1 + dp[i-1][j-1]
            } else {
                iMinus := dp[i-1][j]
                jMinus := dp[i][j-1]
                if iMinus > jMinus {
                    dp[i][j] = iMinus
                } else {
                    dp[i][j] = jMinus
                }
            }
        } 
    }
    return dp[n][m]
}