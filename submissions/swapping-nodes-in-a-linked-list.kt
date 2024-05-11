// https://leetcode.com/problems/swapping-nodes-in-a-linked-list

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
    fun swapNodes(head: ListNode?, k: Int): ListNode? {
        var kthBegin : ListNode? = head
        var kVal : Int = k
        while (kVal > 1) { // 1-indexed 
            kVal--
            kthBegin = kthBegin?.next
        }
        var lastNode : ListNode? = kthBegin
        var kthEnd : ListNode?= head
        while (lastNode?.next != null) {
            kthEnd = kthEnd?.next
            lastNode = lastNode?.next
        }
        kthBegin?.`val` = kthEnd?.`val`.also{kthEnd?.`val` = kthBegin?.`val`}
        return head
    }
}