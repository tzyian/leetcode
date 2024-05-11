// https://leetcode.com/problems/binary-tree-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        stack: List[TreeNode] = []
        node = root
        

        while True:
            while node:
                stack.append(node)
                node = node.left
            if stack:
                curr = stack.pop()
                ans.append(curr.val)
                if curr.right:
                    node = curr.right
            else:
                break
        return ans
