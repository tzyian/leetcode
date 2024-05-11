// https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1

        q = deque()
        q.append(root)
        
        maxsum = -2<<32 + 1
        maxrow = -1
        curr = 0
        
        while q:
            curr += 1
            rowsum = 0
            rowlen = len(q)
            for _ in range(rowlen):
                node = q.popleft()
                if not node:
                    continue
                rowsum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if rowsum > maxsum:
                maxrow = curr
                maxsum = rowsum
        return maxrow
