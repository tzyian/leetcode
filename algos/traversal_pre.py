class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root: TreeNode | None) -> list[int]:
    if not root:
        return []

    ans = []
    stack: list[TreeNode] = [root]
    while stack:
        curr = stack.pop()
        if not curr:
            continue
        ans.append(curr.val)

        ### append rightmost child first so left child is processed first
        # for child in reversed(curr.children):
        #     stack.append(child)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)

    return ans
