// https://leetcode.com/problems/delete-operation-for-two-strings

func minDistance(word1 string, word2 string) int {
    
    n := len(word1)
    m := len(word2)
    dp := make([][]int, n+1)

    for i := 0; i < n+1; i++ {
        dp[i] = make([]int, m+1)
    }

    for i := 1; i < n+1; i++ {
        for j := 1; j < m+1; j++ {
            if word1[i-1] == word2[j-1] {
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

    common := dp[n][m]
    return n - common + m - common
}