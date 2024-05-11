// https://leetcode.com/problems/insertion-sort-list

package main

// type ListNode struct {
// 	Val  int
// 	Next *ListNode
// }

func insertionSortList(head *ListNode) *ListNode {
	dummy := &ListNode{Val: 0}
	dummy.Next = head
	curr := head
	prev := head

	for curr != nil {
		if curr.Val < prev.Val {
			prev.Next = curr.Next
			tempPrev := dummy
			temp := dummy.Next
			for temp.Val <= curr.Val {
				tempPrev = temp
				temp = temp.Next
			}
			tempPrev.Next, curr.Next, curr = curr, temp, prev.Next
		} else {
			prev = curr
			curr = curr.Next
		}
	}
	return dummy.Next
}
