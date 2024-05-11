// https://leetcode.com/problems/minimum-absolute-difference-in-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def in_order_traversal(node):
            if not node:
                return []
            return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)

        if not root:
            return 0
        lst = in_order_traversal(root)
        min_diff = 1e9
        for i in range(1, len(lst)):
            min_diff = min(lst[i] - lst[i-1], min_diff)
        return min_diff
        