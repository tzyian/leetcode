from typing import Optional, List


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
        dfs(node.right)
        ls.append(node.val)

    dfs(root)
    return ls


def postorder_double_push(root):
    if not root:
        return []
    ans, stack = [], [root, root]
    while stack:
        node = stack.pop()
        if stack and stack[-1] is node:
            if node.right:
                stack.append(node.right)
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                stack.append(node.left)
        else:
            ans.append(node.val)
    return ans


def postorderTraversal(root: Optional[TreeNode]) -> List[int]:
    res = []
    stack = [(root, False)]

    while stack:
        node, visited = stack.pop()
        if not node:
            continue
        if visited:
            res.append(node.val)
        else:
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))
    return res


def postorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
    result: List[int] = []
    stack: List[TreeNode] = []
    curr: Optional[TreeNode] = root
    last_visited: Optional[TreeNode] = None

    while stack or curr:
        if curr:
            # go as far left as possible
            stack.append(curr)
            curr = curr.left
        else:
            peek = stack[-1]
            # if right child exists and hasn't been processed, go right
            if peek.right and last_visited is not peek.right:
                curr = peek.right
            else:
                # both children done, process node
                result.append(peek.val)
                last_visited = stack.pop()
    return result
