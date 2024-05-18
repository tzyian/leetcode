struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    explicit ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// @leet start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* doubleIt(ListNode* head) {
        ListNode* back = reverseList(head);
        ListNode* doubledBack = doubleList(back);
        ListNode* newHead = reverseList(doubledBack);
        return newHead;
    }

private:
    
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr || head->next == nullptr) {
            return head;
        }

        ListNode* prev = nullptr;
        ListNode* curr = head;
        ListNode* next;

        
        while (curr != nullptr) {
            next = curr->next;
            curr->next = prev;

            prev = curr;
            curr = next;
        }
        return prev;
    }

    ListNode* doubleList(ListNode* head) {
        if (head == nullptr) {
            return head;
        }

        ListNode* prev = nullptr;
        ListNode* curr = head;
        int carry = 0;

        while (curr != nullptr) {
            int doubled = curr->val * 2 + carry;
            if (doubled > 9) {
                curr->val = doubled % 10;
                carry = doubled / 10;
            } else {
                carry = 0;
                curr->val = doubled;
            }
            prev = curr;
            curr = curr->next;
        }

        if (carry > 0) {
            prev->next = new ListNode(carry);
        }

        return head;

    }
};
// @leet end
