package leetcode

// @leet start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeNodes(head *ListNode) *ListNode {
	sum := 0
	newList := &ListNode{0, nil}
	newTail := newList

	curr := head.Next
	for curr != nil {
		if curr.Val == 0 && sum != 0 {
			newTail.Next = &ListNode{sum, nil}
			newTail = newTail.Next
			sum = 0
		} else {
			sum += curr.Val
		}
		curr = curr.Next
	}
	return newList.Next

}

// @leet end
