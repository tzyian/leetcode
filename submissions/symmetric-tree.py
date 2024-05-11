// https://leetcode.com/problems/symmetric-tree

#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Approaches
Recursive
Iterative (append tuples of (l.l, r.r), (r.l, l.r), pop to check)
Level Order traversal into a list to see if list is symmetric
'''

class Solution:
    # Recursive
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not left and not right:
                return True
            elif (not left) or (not right) or (left.val != right.val):
                return False
            return helper(left.left, right.right) and helper(left.right, right.left)

        return not root or helper(root.left, root.right)

    # #Iterative
    # def isSymmetric(self, root):
    #     if root is None:
    #         return True
    #     stack = [(root.left, root.right)]
    #     while stack:
    #         left, right = stack.pop()
    #         if left is None and right is None:
    #             continue
    #         if left is None or right is None:
    #             return False
    #         if left.val == right.val:
    #             stack.append((left.left, right.right))
    #             stack.append((left.right, right.left))
    #         else:
    #             return False
    #     return True

        




