// https://leetcode.com/problems/minimum-absolute-difference-in-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        inf = 1_000_000
        stack: Stack[TreeNode] = []
        mindiff = inf

        if not root:
            return inf
        
        num1 = 0
        num2 = inf

        # iterative in-order traversal (recursive is usually easier_)
        node = root
        while True:
            if node:
                stack.append(node)
                node = node.left
                
            else:
                while stack:
                    curr = stack.pop()
                    num2, num1 = curr.val, num2
                    mindiff = min(mindiff, abs(num2 - num1))
                    print(f"mindiff is {mindiff}, currv is {curr.val}")
                    node = curr.right 
                    break
                if not node and not stack:
                    break
        return mindiff
        