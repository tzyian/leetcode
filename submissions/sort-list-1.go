// https://leetcode.com/problems/sort-list

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func sortList(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return head
    }

    prev, mid := findMiddle(head)
    prev.Next = nil

    left := sortList(head)
    right := sortList(mid)
    return merge(left, right)

}

func findMiddle(head *ListNode) (*ListNode, *ListNode) {
    // slow = n / 2 + 1 if even number of nodes
    slow := head
    prev := head
    fast := head
    for fast != nil && fast.Next != nil {
        prev = slow
        slow = slow.Next
        fast = fast.Next.Next
    }
    return prev, slow
}

func merge(xs *ListNode, ys *ListNode) *ListNode {

    if ys == nil {
        return xs
    } else if xs == nil {
        return ys
    }
    if xs.Val <= ys.Val {
        xs.Next = merge(xs.Next, ys)
        return xs
    } else {
        ys.Next = merge(ys.Next, xs)
        return ys
    }
}