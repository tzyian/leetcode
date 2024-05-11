// https://leetcode.com/problems/reorder-list

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reorderList(head *ListNode)  {
    // O(n) time and O(1) space

    // edge cases of 0, 1, 2 elements where no ops have to be performed
    if head == nil || head.Next == nil || head.Next.Next == nil {
        return
    }

    // find middle node and node before
    prev, mid := findMiddleNode(head)

    // disconnect prev from mid
    prev.Next = nil

    // reverse the second half
    listTwo := reverseList(mid)

    // merge the two lists together
    mergeTwo(head, listTwo)
}

func findMiddleNode(head *ListNode) (*ListNode, *ListNode) {
    prev := head
    slow := head
    fast := head
    for (fast != nil) && (fast.Next != nil) {
        prev = slow
        slow = slow.Next
        fast = fast.Next.Next
    }
    return prev, slow
}

func reverseList(head *ListNode) *ListNode {
    if head == nil {
        return nil
    }

    var prev *ListNode = nil
    curr := head
    aft := head.Next

    for aft != nil {
        curr.Next = prev
        prev = curr
        curr = aft
        aft = aft.Next
    }
    curr.Next = prev

    return curr
}

func mergeTwo(first *ListNode, second *ListNode) {
    for second != nil {
        temp := first.Next
        first.Next = second
        
        first = second
        second = temp
    }
}