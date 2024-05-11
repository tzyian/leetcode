class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

// @leet start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNodes(ListNode head) {
        ListNode tail = reverseList(head);

        int maxVal = tail.val;
        ListNode prev = tail;
        ListNode node = tail.next;

        while (node != null) {
            if (node.val >= maxVal) {
                maxVal = node.val;
                prev = node;
            } else {
                prev.next = node.next;
            }

            node = node.next;
        }

        ListNode newHead = reverseList(tail);

        return newHead;

    }

    private ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode prev = null;
        ListNode node = head;

        while (node != null) {
            ListNode temp = node.next;
            node.next = prev;
            prev = node;
            node = temp;
        }

        return prev;

    }
}
// @leet end
