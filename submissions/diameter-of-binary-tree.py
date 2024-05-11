// https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        '''
        return height of current node, max diameter within subtree
        (height, dia)
        '''
        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
            if not node:
                return -1, 0

            leftheight, leftdiam = dfs(node.left)
            rightheight, rightdiam = dfs(node.right)


            # subtree_diam = 0
            # subtree_height = 0
            # if leftheight == 0:
            #     subtree_diam = rightheight + 1
            #     subtree_height = rightheight + 1
            # elif rightheight == 0:
            #     subtree_diam = leftheight + 1
            #     subtree_height = leftheight + 1
            # else:
            #     subtree_height = max(leftheight, rightheight) + 1
            #     subtree_diam = leftheight + rightheight + 2

            subtree_diam = leftheight+rightheight+2
            subtree_height = max(leftheight, rightheight) + 1
            max_diam = max(subtree_diam, leftdiam, rightdiam)
            return (subtree_height, max_diam)
        
        return dfs(root)[1]