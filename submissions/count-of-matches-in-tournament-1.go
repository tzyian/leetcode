// https://leetcode.com/problems/count-of-matches-in-tournament

func numberOfMatches(n int) int {
    remaining := n
    matches := 0
    for remaining > 1 {
        matches += remaining / 2
        if remaining % 2 == 0 {
            remaining /= 2
        } else {
            remaining = remaining / 2 + 1
        }
        
    }
    return matches
}