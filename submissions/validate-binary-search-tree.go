// https://leetcode.com/problems/validate-binary-search-tree

import "math"

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func isValidBST(root *TreeNode) bool {
	return isValidSubtree(root, math.MinInt, math.MaxInt)
}

func isValidSubtree(root *TreeNode, minVal int, maxVal int) bool {
	if root == nil {
		return true
	}

	if root.Val >= maxVal || root.Val <= minVal {
		return false
	}

	return isValidSubtree(root.Left, minVal, root.Val) && isValidSubtree(root.Right, root.Val, maxVal)

}
