// https://leetcode.com/problems/predict-the-winner

const (
    P1 int = 1
    P2     = -1
)

// dp over the difference in score.
// if >= 0, player 1 has more points (p1 wins if diff is 0)
// if <0, player 2 has more points
    
func PredictTheWinner(nums []int) bool {
    p1HigherScore := helper(nums, 1)
    return p1HigherScore >= 0
}

// return diff in score
func helper(nums []int, player int) int {
    n := len(nums)
    if n == 0 {
        return 0
    }
    
    // If p1 (player = 1), then add to diff. If p2 (player = -1), subtract from diff.
    startVal := nums[0] * player
    endVal := nums[n - 1] * player

    takeStart := startVal + helper(nums[1:n], -player)
    takeEnd := endVal + helper(nums[:n-1], -player)
    
    if player == P2 {
        // min of both
        if takeStart <= takeEnd {
            return takeStart
        }
        return takeEnd
    } else {
        // max of both
        if takeStart >= takeEnd {
            return takeStart
        }
        return takeEnd
    }
    
}