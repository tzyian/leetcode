# @leet start
from collections import Counter, defaultdict
from typing import List

"""
If diameter is odd, there can be only 1 MHT (the node at diameter)
If diameter is even, there are only 2 MHT (the 2 nodes at diameter)

1.
Eat edges

2.
DFS from node to find leaf node A
DFS from leaf node A to leaf node B to find further diameter.
Construct path from A to B. Take midpoint of the path.
"""


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = [set() for _ in range(n)]

        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        leaves = [i for i in range(n) if len(adj[i]) == 1]

        counted_nodes = n
        while counted_nodes > 2:
            counted_nodes -= len(leaves)

            new_leaves = []

            for i in leaves:
                j = adj[i].pop()
                adj[j].remove(i)
                if len(adj[j]) == 1:
                    new_leaves.append(j)
            leaves = new_leaves

        return leaves


# @leet end
