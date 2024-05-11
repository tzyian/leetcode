// https://leetcode.com/problems/same-tree

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        return (p == null && q == null) 
            ? true
            : p == null || q == null
            ? false
            : p.val == q.val
            ? isSameTree(p.left, q.left) && isSameTree(p.right, q.right)
            : false;
    }
}