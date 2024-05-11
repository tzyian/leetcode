// https://leetcode.com/problems/minimum-time-visiting-all-points

func minTimeToVisitAllPoints(points [][]int) int {
    time := 0
    for i := 1; i < len(points); i++ {
        prev := points[i-1]
        curr := points[i]
        dx := abs(curr[0] - prev[0])
        dy := abs(curr[1] - prev[1])
        diags := min(dx, dy)
        // dx -= diags
        // dy -= diags
        time += dx + dy - diags
    
    }
    return time
}

func min(a int, b int) int {
    if a < b {
        return a
    }
    return b
}

func abs(a int) int {
    if a < 0 {
        return -a
    }
    return a
}