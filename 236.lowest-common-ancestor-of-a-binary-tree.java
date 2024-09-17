// @leet start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q) {
            return root;
        } 

        TreeNode inLeft = lowestCommonAncestor(root.left, p, q);
        TreeNode inRight = lowestCommonAncestor(root.right, p, q);

        if (inLeft != null && inRight != null) {
            return root;
        } else if (inLeft != null) {
            return inLeft;
        } else if (inRight != null) {
            return inRight;
        }
        
        return null;
    }
}
// @leet end
