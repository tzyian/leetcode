# @leet start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:

        start_path = []
        dest_path = []

        def find_node(
            node: Optional[TreeNode], target_val: int, dirs: list[str]
        ) -> bool:
            if not node:
                return False

            if node.val == target_val:
                return True

            dirs.append("L")
            if find_node(node.left, target_val, dirs):
                return True
            dirs.pop()

            dirs.append("R")
            if find_node(node.right, target_val, dirs):
                return True
            dirs.pop()

            return False

        # Find path to start, path to dest
        find_node(root, startValue, start_path)
        find_node(root, destValue, dest_path)

        # Remove common prefix
        i = 0
        while i < min(len(start_path), len(dest_path)):
            if start_path[i] == dest_path[i]:
                i = i + 1
                continue
            break

        # Replace path to start with "U", and path to dest remains
        path = ["U"] * len(start_path[i:]) + dest_path[i:]
        ans = "".join(path)
        return ans


# @leet end
