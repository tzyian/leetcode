from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recursive(root: TreeNode | None) -> list[int]:
    ls = []

    def dfs(node: TreeNode | None) -> None:
        if not node:
            return

        dfs(node.left)
        ls.append(node.val)
        dfs(node.right)

    dfs(root)
    return ls


def inorder_traversal(root: TreeNode | None) -> list[int]:
    ans = []
    stack = []
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        ans.append(curr.val)
        curr = curr.right

    return ans
