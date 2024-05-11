// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

 // Given unique values and correct traversals
func buildTree(preorder []int, inorder []int) *TreeNode {
    n := len(preorder)
    if n == 0 {
        return nil
    } 

    root := TreeNode{Val: preorder[0]}

    for i, ele := range inorder {
        if ele == root.Val {
            root.Left = buildTree(preorder[1:i+1], inorder[:i])
            root.Right = buildTree(preorder[i+1:], inorder[i+1:])
            break
        }
    }
    return &root
}
