package leetcode

// @leet start
func shortestCommonSupersequence(str1 string, str2 string) string {
	n, m := len(str1), len(str2)
	dp := make([][]int, n+1)

	// TC: O(n * m)
	// SC: O(n * m)
	// This requires having the 2d DP table but does not require storing the strings in the table themselves

	// dp[i][0] holds the length of str1[:i]
	for i := range n + 1 {
		dp[i] = make([]int, m+1)
		dp[i][0] = i
	}
	// dp[0][j] holds the length of str2[:j]
	for j := range m + 1 {
		dp[0][j] = j
	}

	// DP using LCS
	// Except you add characters for both cases
	for i := 1; i <= n; i++ {
		for j := 1; j <= m; j++ {
			if str1[i-1] == str2[j-1] {
				dp[i][j] = 1 + dp[i-1][j-1]
			} else {
				dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
			}
		}
	}

	// reconstruct the string from the dp table
	superseq := make([]byte, 0, dp[n][m])
	i, j := n, m
	for i > 0 && j > 0 {
		if str1[i-1] == str2[j-1] {
			superseq = append(superseq, str1[i-1])
			i--
			j--
		} else if dp[i-1][j] < dp[i][j-1] {
			superseq = append(superseq, str1[i-1])
			i--
		} else {
			superseq = append(superseq, str2[j-1])
			j--
		}
	}

	// append remaining characters
	for i > 0 {
		superseq = append(superseq, str1[i-1])
		i--
	}
	for j > 0 {
		superseq = append(superseq, str2[j-1])
		j--
	}

	// reverse the supersequence
	for left, right := 0, len(superseq)-1; left < right; left, right = left+1, right-1 {
		superseq[left], superseq[right] = superseq[right], superseq[left]
	}
	return string(superseq)
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// @leet end

