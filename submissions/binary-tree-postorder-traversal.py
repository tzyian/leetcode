// https://leetcode.com/problems/binary-tree-postorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        # def helper(root: Optional[TreeNode]) -> None:
        #     if root:
        #         helper(root.left)
        #         helper(root.right)
        #         ans.append(root.val)
        
        # helper(root)
        # return ans

        if not root:
            return ans
        
        stack: List[TreeNode] = []

        while True:
            while root:
                if root.right:
                    stack.append(root.right)
                stack.append(root)

                root = root.left

            root = stack.pop()

            if root.right and stack and stack[-1] == root.right:
                stack.pop()
                stack.append(root)
                root = root.right
            else:
                ans.append(root.val)
                root = None

            if not stack:
                break

            
          
        return ans


