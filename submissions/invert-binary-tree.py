// https://leetcode.com/problems/invert-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        if not root.left and not root.right:
            return root
        elif not root.left:
            root.left = self.invertTree(root.right)
            root.right = None
            return root
        elif not root.right:
            root.right = self.invertTree(root.left)
            root.left = None
            return root
        else:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root
        ### for array representation
        # layer = 0
        # newRoot = []
        # i = 0
        # index = 0
        # while index < len(root):
        #     for i in range(index, 2 ** layer, -1):
        #         newRoot[index] = root[i]
        #         index += 1
        #     layer += 1
        # return newRoot
