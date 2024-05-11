package local

type ListNode struct {
	Val  int
	Next *ListNode
}

// @leet start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNodes(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}

	var stack []*ListNode
	node := head
	for node.Next != nil {
		stack = append(stack, node)
		node = node.Next
	}

	newHead := node
	maxVal := node.Val

	for len(stack) > 0 {
		node = stack[len(stack)-1]

		if node.Val >= maxVal {
			maxVal = node.Val
			node.Next = newHead
			newHead = node
		}

		stack = stack[:len(stack)-1]
	}

	return newHead
}

// @leet end

