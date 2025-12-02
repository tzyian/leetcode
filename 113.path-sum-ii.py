# @leet imports start
from typing import List, Optional, Tuple


# @leet imports end
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @leet start
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        if not root:
            return []
        if not root.left and not root.right and targetSum == root.val:
            return [[root.val]]

        left = self.pathSum(root.left, targetSum - root.val)
        right = self.pathSum(root.right, targetSum - root.val)
        return [[root.val] + path for path in left + right]


# @leet end


# Definition for a binary tree node.
class SolutionBad:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def helper(
            root: Optional[TreeNode], targetSum: int
        ) -> Tuple[bool, List[List[int]]]:

            if not root:
                return False, []
            if not root.left and not root.right and targetSum == root.val:
                return True, [[root.val]]

            leftForm, leftRes = helper(root.left, targetSum - root.val)
            rightForm, rightRes = helper(root.right, targetSum - root.val)

            ans = []
            if leftForm:
                left = [[root.val] + path for path in leftRes]
                ans.extend(left)
            if rightForm:
                right = [[root.val] + path for path in rightRes]
                ans.extend(right)

            return leftForm or rightForm, ans

        _, res = helper(root, targetSum)
        return res

