# @leet imports start
from typing import List, Optional

# @leet imports end


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(start: int, stop: int) -> Optional[TreeNode]:
            if start > stop:
                return

            mid = start + (stop - start) // 2
            node = TreeNode(nums[mid])
            node.left = helper(start, mid - 1)
            node.right = helper(mid + 1, stop)
            return node

        n = len(nums)
        return helper(0, n - 1)


# @leet end

