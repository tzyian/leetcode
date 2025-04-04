from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @leet start
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # dfs
        # each node marks the deepest heights of their subtrees
        # O(n) time, O(n) recursion space

        def helper(node: TreeNode | None) -> tuple[int, TreeNode | None]:
            if not node:
                return 0, None
            left, llca = helper(node.right)
            right, rlca = helper(node.left)

            if left > right:
                return left + 1, llca
            elif left < right:
                return right + 1, rlca
            else:
                return left + 1, node

        _, ans = helper(root)
        return ans


# @leet end

