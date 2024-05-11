// https://leetcode.com/problems/delete-and-earn

func deleteAndEarn(nums []int) int {
    // O(max(nums) - min(nums) ) time
    points := make([]int, 2 * 10_000 + 1)
    maxVal := 0
    minVal := 10_001 // as long as greater than constraint

    // transform nums into points.
    // since if you take n, you can get all points of worth n
    // and n-1 and n+1 can only be deleted once
    for _, val := range nums {
        points[val] += val
        minVal = min(val, minVal)
        maxVal = max(val, maxVal)
    }

    take := 0
    notTake := 0

    for _, val := range points[minVal: maxVal + 1] {
        tempTake := take
        take = notTake + val
        notTake = max(tempTake, notTake)
    }

    return max(take, notTake)
}

func max(a int, b int) int {
    if a > b {
        return a
    } 
    return b
}

func min(a int, b int) int {
    if a < b {
        return a
    }
    return b
}