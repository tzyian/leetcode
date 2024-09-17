package leetcode

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// @leet start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func createBinaryTree(descriptions [][]int) *TreeNode {
	// Where n is number of nodes,
	// TC O(n), SC O(n)
	nodes := make(map[int]*TreeNode)
	orphans := make(map[int]struct{})

	// Make nodes
	for _, desc := range descriptions {
		p := desc[0]
		c := desc[1]
		// Make a new node for parent
		if _, ok := nodes[p]; !ok {
			newNode := &TreeNode{Val: p}
			nodes[p] = newNode
			orphans[p] = struct{}{}
		}
		// Make a new node for child
		if _, ok := nodes[c]; !ok {
			newNode := &TreeNode{Val: c}
			nodes[c] = newNode
			orphans[c] = struct{}{}
		}
	}

	// Assign values
	for _, desc := range descriptions {
		p := desc[0]
		c := desc[1]
		isLeft := desc[2]

		if isLeft == 1 {
			nodes[p].Left = nodes[c]
		} else {
			nodes[p].Right = nodes[c]
		}
		delete(orphans, c)
	}

	for k, _ := range orphans {
		return nodes[k]
	}
	// Guaranteed to return above since only 1 root
	return nil

}

// @leet end
