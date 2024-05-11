// https://leetcode.com/problems/house-robber


func rob(nums []int) int {
    take := 0
    noTake := 0

    for i := range nums {
        temp := take
        take = nums[i] + noTake
        noTake = max(temp, noTake)
    }

    return max(take, noTake)
}


func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}