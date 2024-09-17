from typing import List, Optional


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
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        forest = []
        del_set = set(to_delete)

        def process_node(node: TreeNode) -> Optional[TreeNode]:
            if not node:
                return None

            node.left = process_node(node.left)
            node.right = process_node(node.right)

            if node.val in del_set:
                if node.left:
                    forest.append(node.left)
                if node.right:
                    forest.append(node.right)
                return None
            return node

        root = process_node(root)

        if root:
            forest.append(root)

        return forest


# @leet end
