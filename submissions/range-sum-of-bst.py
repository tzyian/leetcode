// https://leetcode.com/problems/range-sum-of-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def __init__(self):
    self.count = 0
    
  def rangeSumBST(self, node, low, high) -> int:
    self.count = 0
    self.helper(node, low, high)
    return self.count

  def helper(self, node, low, high):
    if not node:
      return
      
    if low <= node.val and node.val <= high:
      self.count += node.val      
      
    if low < node.val and node.val < high:
      # strictly within
      self.helper(node.left, low, high)
      self.helper(node.right, low, high)
    elif node.val <= low:
      # only check right tree
      self.helper(node.right, low, high)
    elif node.val >= high:
      # only check left tree
      self.helper(node.left, low, high)
      