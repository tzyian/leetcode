// https://leetcode.com/problems/kth-smallest-element-in-a-bst

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func kthSmallest(root *TreeNode, k int) int {
    // left, found, ans
    ans := []int{k, 0}
    helper(root, ans)
    return ans[1]
}

func helper(root *TreeNode, k []int) {
    if root == nil {
        return
    }
    
    if k[0] > 0 {
        helper(root.Left, k)
    } else {
        return
    }

    k[0]--
    if k[0] == 0 {
        k[1] = root.Val
        return
    }
    

    if k[0] > 0 {
        helper(root.Right, k)
    }

}