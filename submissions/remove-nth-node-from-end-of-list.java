// https://leetcode.com/problems/remove-nth-node-from-end-of-list

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode back = dummy;
        ListNode front = dummy;
        while (n > 0) {
            front = front.next;
            n--;
        }
        
        while (front.next != null) {
            front = front.next;
            back = back.next;
        }

        back.next = back.next.next;
        return dummy.next;
    }
}