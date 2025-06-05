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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        inf = 10**9
        best = -inf

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal best

            if not node:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            rooted = node.val + left + right
            best = max(best, rooted)
            return node.val + max(left, right)

        dfs(root)
        return best


# @leet end

t = TreeNode(1, TreeNode(2), TreeNode(3))
x = Solution().maxPathSum(t)
print(x)

