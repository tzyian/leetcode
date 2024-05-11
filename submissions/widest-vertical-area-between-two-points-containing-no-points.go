// https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points

func maxWidthOfVerticalArea(points [][]int) int {
    slices.SortFunc(points, func(a, b []int) int {
        if a[0] < b[0] {
            return -1
        } else if (a[0] == b[0]) {
            return 0
        }
        return 1
    })
    maxVert := 0
    for i := 1; i < len(points); i++ {
        maxVert = max(points[i][0] - points[i-1][0], maxVert)
    }
    return maxVert
}

func max(a, b int) int {
    if a < b {
        return b
    }
    return a
}