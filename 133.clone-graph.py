# @leet start
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None
        nodes = dict()

        def helper(curr: Optional[Node]) -> Optional[Node]:
            if not curr:
                return None

            if curr.val in nodes:
                return nodes[curr.val]

            copied = Node(curr.val)

            nodes[curr.val] = copied

            for nb in curr.neighbors:
                cp_nb = helper(nb)
                copied.neighbors.append(cp_nb)

            return copied

        return helper(node)


# @leet end

