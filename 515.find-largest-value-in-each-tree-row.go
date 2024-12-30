package leetcode

import "math"

// @leet start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func largestValues(root *TreeNode) []int {
  ans := make([]int, 0)

  if root == nil {
    return ans
  }

  queue := make([]*TreeNode, 0)
  curr := root
  queue = append(queue, curr)

  for len(queue) > 0 {
    n := len(queue)
    row := make([]int, 0)

    for _ = range(n) {
      curr = queue[0]
      queue = queue[1:]
      row = append(row, curr.Val)

      if curr.Left != nil {
        queue = append(queue, curr.Left)
      }
      if curr.Right != nil {
        queue = append(queue, curr.Right)
      }
    }
    ans = append(ans, maxArr(row))
  }
  return ans
    
}

func maxArr(arr []int) int {
  maxVal := math.MinInt
  for _, ele := range arr {
    if ele > maxVal {
      maxVal = ele
    }
  }
  return maxVal
}
// @leet end
