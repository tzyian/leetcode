// https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list

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
    fun pairSum(head: ListNode?): Int {
        val arrlist = mutableListOf<Int>().also {
            if (head != null) {
                it.add(head.`val`)
            }
        }
        var node = head?.next

        while (true) {
            if (node == null) {
                break
            }
            arrlist.add(node.`val`)
            node = node.next
        }

        var max: Int = Integer.MIN_VALUE
        for (i in 0..arrlist.size / 2) {
            val check = arrlist[i] + arrlist[arrlist.size - 1 - i]
            if (check > max ) {
                max = check
            }
        }

        return max
    }

}