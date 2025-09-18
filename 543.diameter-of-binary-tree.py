from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0

        def height(root: Optional[TreeNode]) -> int:
            nonlocal best

            if not root:
                return 0

            left = height(root.left)
            right = height(root.right)
            best = max(best, left + right)

            return 1 + max(left, right)

        height(root)
        return best


# @leet end
