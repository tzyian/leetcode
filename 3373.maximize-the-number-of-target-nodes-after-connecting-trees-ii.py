from collections import defaultdict, deque
from typing import List


# @leet start
class Solution:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> List[int]:
        # 1. for tree 1 node i, find nodes which have even number of edges to it
        # (run bfs on every node)

        # 2. on tree 2, find diameter. if diameter is even, find 2nd longest path
        # the node on tree 2 which has the most odd dist nodes is what you're connecting to

        # even on tree 1 + odd on tree 2 = target for tree 1 node i


        # NOTE: this will TLE.
        # Doing bfs twice to find nodes at edges of diameter will not find the correct answer due to skewed trees.

        def construct_adj(edges: list[list[int]]) -> defaultdict[int, list[int]]:
            adj = defaultdict(list)
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj


        def bfs(root: int, adj: dict[int, list[int]], criterion: int) -> int:
            # idt it is more efficient to precompute
            satisf = 0
            queue = deque()
            visited = set()
            visited.add(root)

            queue.append(root)
            dist = 0

            while queue:
                nq = len(queue)
                for _ in range(nq):
                    curr = queue.popleft()
                    visited.add(curr)
                    for v in adj[curr]:
                        if v not in visited:
                            queue.append(v)

                # add count of nodes which have paths of even/odd lengths respectively
                dist = (dist + 1) & 1
                if dist == criterion:
                    satisf += len(queue)

            return satisf


        def find_most_odd_paths(adj: dict[int, list[int]]) -> int:
            odds = 0
            for v in adj:
                new_odds = bfs(v, adj, 1)
                odds = max(odds, new_odds)
            return odds

        ans = []
        adj1 = construct_adj(edges1)
        adj2 = construct_adj(edges2)

        most_odd_paths_from_node = find_most_odd_paths(adj2)

        for u in sorted(adj1):
            evens = bfs(u, adj1, 0)
            # +1 for evens to include itself
            ans.append(1 + evens + most_odd_paths_from_node)

        return ans


# @leet end

e1 = [[0,1],[0,2],[2,3],[2,4]]
e2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
x = Solution().maxTargetNodes(e1, e2)
print(x)
