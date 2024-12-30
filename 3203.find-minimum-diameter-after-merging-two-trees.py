# @leet start
from collections import defaultdict, deque
from typing import List

AdjList = dict[int, set[int]]


class Solution:
    def minimumDiameterAfterMerge(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> int:
        adjlist1 = self.adjlist(edges1)
        adjlist2 = self.adjlist(edges2)

        if not edges1 and not edges2:
            # apparently if no edges, then it's a single node tree here??
            return 1

        l1 = self.calc_levels(adjlist1)
        l2 = self.calc_levels(adjlist2)

        middle = l1 // 2 + l2 // 2 + 1
        # - 1 because find diameter instead of max levels
        return max(l1 - 1, l2 - 1, middle)

    def adjlist(self, edges: list[list[int]]) -> AdjList:
        adjlist = defaultdict(set[int])
        for u, v in edges:
            adjlist[u].add(v)
            adjlist[v].add(u)

        return adjlist

    def calc_levels(self, tree: AdjList) -> int:
        if not tree:
            return 1

        node = next(iter(tree.keys()))
        node, _ = self.bfs(node, tree)
        _, levels = self.bfs(node, tree)
        return levels

    def bfs(self, node: int, tree: AdjList) -> tuple[int, int]:
        # NOTE: do not do `if not node` because if node == 0 then it fails...
        if node == -1:
            return -1, 0
        queue = deque([node])
        levels = 0
        curr = node
        visited = set([curr])

        while queue:
            n = len(queue)
            for _ in range(n):
                curr = queue.popleft()
                for nb in tree[curr]:
                    if nb not in visited:
                        visited.add(nb)
                        queue.append(nb)
            levels += 1

        return curr, levels


# @leet end

