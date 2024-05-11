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
       if (head == null || head?.next == null) {
           return head
       }
       var newHead = head?.next
       var temp = head?.next?.next
       newHead?.next = head
       head?.next = swapPairs(temp)
       return newHead
    }

}