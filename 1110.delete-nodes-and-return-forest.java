
// @leet start
/**
 * Definition for a binary tree node. public class TreeNode { int val; TreeNode left; TreeNode
 * right; TreeNode() {} TreeNode(int val) { this.val = val; } TreeNode(int val, TreeNode left,
 * TreeNode right) { this.val = val; this.left = left; this.right = right; } }
 */
import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Set;
import java.util.stream.Collectors;

class Solution {
    public List<TreeNode> delNodes(TreeNode root, int[] to_delete) {
        Set<TreeNode> forest = new HashSet<>();
        Set<Integer> unwanted = Arrays.stream(to_delete).boxed().collect(Collectors.toSet());

        Queue<TreeNode> queue = new LinkedList<>();

        if (!unwanted.contains(root.val)) {
            forest.add(root);
        }
        queue.add(root);

        while (!queue.isEmpty()) {
            TreeNode curr = queue.poll();
            if (curr == null) {
                continue;
            }

            queue.add(curr.left);
            queue.add(curr.right);

            TreeNode left = curr.left;
            TreeNode right = curr.right;

            // Remove children from parent if children are unwanted
            if (curr.left != null && unwanted.contains(curr.left.val)) {
                curr.left = null;
            }
            if (curr.right != null && unwanted.contains(curr.right.val)) {
                curr.right = null;
            }

            // Add children to forest if parent is unwanted
            if (curr.left != null && unwanted.contains(curr.val)) {
                forest.add(left);
            }

            if (curr.right != null && unwanted.contains(curr.val)) {
                forest.add(right);
            }
        }

        List<TreeNode> ans = forest.stream().toList();
        return ans;
    }
}
// @leet end
