// https://leetcode.com/problems/palindrome-linked-list/description/
//
// @leet start
// class ListNode {
//     int val;
//     ListNode next;
//     ListNode() { }
//     ListNode(int val) { this.val = val; }
//     ListNode(int val, ListNode next) {
//         this.val = val;
//         this.next = next;
//     }
// }

class Solution {
    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null) {
            return true;
        }

        // A separate findLength iteration just for clarity;
        int n = findLength(head);

        // find midpoint
        ListNode mid = findMid(head);

        // although a mid = fast == null ? mid : mid.next will suffice
        if (n % 2 != 0) {
            mid = mid.next;
        }

        // reverse latter half
        mid = reverse(mid);

        // iterate from start and midpoint
        boolean ans = iteratePalindrome(head, mid, n);

        return ans;
    }

    private int findLength(ListNode head) {
        int length = 0;
        ListNode curr = head;
        while (curr != null) {
            length++;
            curr = curr.next;
        }
        return length;
    }

    private ListNode findMid(ListNode head) {
        ListNode curr = head;
        ListNode fast = curr;

        while (fast != null && fast.next != null) {
            curr = curr.next;
            fast = fast.next.next;
        }

        return curr;
    }

    private ListNode reverse(ListNode head) {
        ListNode curr = head;
        ListNode prev = null;
        ListNode temp = null;

        while (curr != null) {
            temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
        }

        return prev;
    }

    private boolean iteratePalindrome(ListNode head, ListNode mid, int n) {
        ListNode first = head;

        while (mid != null) {
            if (first.val != mid.val) {
                return false;
            }
            first = first.next;
            mid = mid.next;
        }
        return true;
    }
}
// @leet end
