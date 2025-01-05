package leetcode

// @leet start
func waysToSplitArray(nums []int) int {
  n := len(nums)
  ans := 0

  psums := make([]int, n)
  psums[0] = nums[0]
  for i := 1; i < n; i++ {
    psums[i] = nums[i] + psums[i - 1]
  }

  for i := 0; i < n - 1; i++ {
    is_valid := psums[i] >= psums[n-1] - psums[i]
    if is_valid {
      ans++
    }
  }
  return ans
    
}
// @leet end
