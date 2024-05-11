// https://leetcode.com/problems/frog-jump

func canCross(stones []int) bool {
    // O(n^2) TC, O(n^2) SC
    n := len(stones)

    // easiest way to take care of edge case
    if n >= 2 {
        if stones[1] - stones[0] != 1 {
            return false
        }
    }

    dp := make([]map[int]struct{}, n)

    // i is index of stone frog is on
    // start from 1 because first jump has to be 1 unit
    for i := 1; i < n; i++ {
        // j is the index of the stone it was previously at
        // dp[i] is the set of distances taken to reach stone[i]
        dp[i] = make(map[int]struct{}, n)
        
        // first jump has to be 1 unit to set first jump
        dp[1][1] = struct{}{}  

        for j := 1; j < i; j++ {
            diff := stones[i] - stones[j]
            // check k-1, k or k+1
            _, okMinusOne := dp[j][diff-1]
            _, okEquals := dp[j][diff]
            _, okPlusOne := dp[j][diff+1]
            if okMinusOne || okEquals || okPlusOne {
                dp[i][diff] = struct{}{}
            }
        }
    }
    return len(dp[n-1]) > 0
}