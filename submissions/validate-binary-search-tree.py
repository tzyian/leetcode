// https://leetcode.com/problems/validate-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        lastChecked = -float('inf')
        nextChecked = -float('inf')

        def compare(node) -> bool:
            nonlocal lastChecked, nextChecked
            lastChecked = nextChecked
            nextChecked = node.val
            return nextChecked > lastChecked


        '''Morris'''
        current = root
    
        while current:
            # If no left subtree, then just move right
            # Or if this is the very last node in the left subtree, then move right BACK to the root of the subtree. So every node is connected to the next node
            if current.left == None:

                if not compare(current):
                    return False


                current = current.right
            else:
                
                # Find predecessor
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right

                # Predecessor is not linked to curr, then link it and explore curr.left
                if predecessor.right == None:
                    predecessor.right = current
                    # preorder visit goes here
                    current = current.left

                # Predecessor is linked to curr. Left subtree has already been explored. Unlink predecessor. Then explore right subtree.
                
                else:
                    predecessor.right = None

                    if not compare(current):
                        return False

                    current = current.right

        return True

