from collections import defaultdict
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # essentially, check whether there is a cycle
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        stack = [(0, -1)]
        while stack:
            node, parent = stack.pop()
            if node in visited:
                return False
            visited.add(node)
            for neighbor in graph[node]:
                # since undirected, we need to avoid going back to parent
                if neighbor != parent:
                    stack.append((neighbor, node))
        return len(visited) == n
