// https://leetcode.com/problems/binary-tree-preorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''Morris'''
        ans = []

        current = root

        while current:
            # If no left subtree, then just move right
            # Or if this is the very last node in the left subtree, then move right BACK to the root of the subtree. So every node is connected to the next node
            if current.left == None:
                ans.append(current.val)
                current = current.right
            else:
                
                # Find predecessor
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right

                # Predecessor is not linked to curr, then link it and explore curr.left
                if predecessor.right == None:
                    predecessor.right = current
                    ans.append(current.val)
                    # to do inorder, move the visit to the else block
                    current = current.left

                # Predecessor is linked to curr. Left subtree has already been explored. Unlink predecessor. Then explore right subtree.
                
                else:
                    predecessor.right = None
                    # inorder visit goes here
                    current = current.right
        return ans






        '''Iterative'''
        # ans = []
        # stack: List[TreeNode] = []
        # node = root

        # while True:
        #     while node:
        #         ans.append(node.val)
        #         stack.append(node)
        #         node = node.left
        #     if stack:
        #         curr = stack.pop()
        #         # inorder visit goes here
        #         if curr.right:
        #             node = curr.right
        #     else:
        #         break
        # return ans

        '''Recursive'''
        # ans = []
        # def helper(node):
        #     if not node:
        #         return
        #     ans.append(node.val)
        #     helper(node.left)
        #     helper(node.right)

        # helper(root)
        # return ans


