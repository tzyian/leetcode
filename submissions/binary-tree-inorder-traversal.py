// https://leetcode.com/problems/binary-tree-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Note that the in-order traversal of a binary tree is a sorted linked list. To flatten a binary tree, just don't reset in the last else block.

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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
                    current = current.left

                # Predecessor is linked to curr. Left subtree has already been explored. Unlink predecessor. Then explore right subtree.
                
                else:
                    predecessor.right = None
                    ans.append(current.val)
                    # to do preorder, just move the visit from here to the if block
                    current = current.right
        return ans






        '''Iterative'''
        # ans = []
        # stack: List[TreeNode] = []
        # node = root

        # while True:
        #     while node:
        #         stack.append(node)
        #         node = node.left
        #     if stack:
        #         curr = stack.pop()
        #         ans.append(curr.val)
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
        #     helper(node.left)
        #     ans.append(node.val)
        #     helper(node.right)

        # helper(root)
        # return ans


