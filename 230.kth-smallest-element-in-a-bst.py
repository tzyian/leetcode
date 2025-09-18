# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @leet start
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in-order traversal, take the kth value
        if not root:
            return -1

        ans = 0
        stack = []

        curr = root
        while (curr or stack) and k > 0:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            ans = curr.val
            k -= 1
            curr = curr.right

        return ans


# @leet end
