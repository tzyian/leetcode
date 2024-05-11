// https://leetcode.com/problems/leaf-similar-trees

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

 // adapted from https://leetcode.com/problems/leaf-similar-trees/solutions/198179/0ms-parallel-iterative-in-order-traversals-in-c/?envType=daily-question&envId=2024-01-09
func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {
    if root1 == root2 {
        // same tree
        return true
    } else if root1 == nil || root2 == nil {
        // roo1 != root2, so if either is nil, then not same
        return false
    }
    s1 := make([]*TreeNode, 1)
    s1[0] = root1
    s2 := make([]*TreeNode, 1)
    s2[0] = root2

    for len(s1) != 0 && len(s2) != 0 {
        var n1, n2 *TreeNode
        n1, s1 = nextLeaf(s1)
        n2, s2 = nextLeaf(s2)
        if n1.Val != n2.Val {
            return false
        }
    }
    return len(s1) == 0 && len(s2) == 0
}


func pop(s []*TreeNode) (*TreeNode, []*TreeNode) {
    n := len(s)
    if n == 0 {
        return nil, nil
    }
    return s[n-1], s[:n-1]
}

func nextLeaf(s []*TreeNode) (*TreeNode, []*TreeNode) {
    var node *TreeNode
    node, s = pop(s)
    for node.Left != nil || node.Right != nil {
        if node.Left != nil {
            if node.Right != nil {
                s = append(s, node.Right)
            }
            node = node.Left
        } else {
            node = node.Right
        }
    }
    return node, s
}