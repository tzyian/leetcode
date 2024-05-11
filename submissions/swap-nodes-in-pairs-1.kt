// https://leetcode.com/problems/swap-nodes-in-pairs

/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun swapPairs(head: ListNode?): ListNode? {
        return reverseKGroup(head, 2)
    }

    fun reverseKGroup(head: ListNode?, k: Int): ListNode? {

        if (k == 1) {
            return head
        }

        var listHead : ListNode? = null

        var prevGroup: ListNode? = ListNode(0)
        prevGroup?.next = head
        var tailSwap = head // current list that is being checked

        while (true) {
            for (i in 1 until k) {
                if (tailSwap?.next == null) {
                    return listHead ?: head
                }
                tailSwap = tailSwap?.next // the last node of a swap group
            }

            var groupHead = prevGroup?.next
            var groupTail = tailSwap
            var nextGroup: ListNode? = tailSwap?.next

            var dummy = reverseGroup(groupHead, groupTail)
            if (listHead == null) {
                listHead = dummy.first
            }
            prevGroup?.next = dummy.first
            prevGroup = dummy.second
            tailSwap = nextGroup

        }
        return listHead ?: head
    }

    fun reverseGroup(start: ListNode?, end: ListNode?): Pair<ListNode?, ListNode?> {
        val stop = end?.next
        var curr: ListNode? = start
        var next: ListNode? = null
        var prev: ListNode? = null

        while (curr != stop) {
            next = curr?.next
            curr?.next = prev
            prev = curr
            curr = next
        }
        start?.next = stop
        return Pair(prev, start) 
        // prev is the head of the reversed group, start is the tail
    }

}