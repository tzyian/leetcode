// https://leetcode.com/problems/detonate-the-maximum-bombs


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        # i explodes j, or j in radius of explosion i
        def in_radius(i: int, j: int) -> bool:
            dx = bombs[j][0] - bombs[i][0]
            dy = bombs[j][1] - bombs[i][1]
            r = bombs[i][2]
            return dx ** 2 + dy ** 2 <= r ** 2

        def construct_adj_list():
            n = len(bombs)
            adj_list = [[]for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    if in_radius(i, j):
                        adj_list[i].append(j)
            return adj_list

        def dfs(i, visited, adj_list):
            visited.add(i)
            for j in adj_list[i]:
                if j not in visited:
                    visited.add(j)
                    dfs(j, visited, adj_list)

        n = len(bombs)
        adj_list = construct_adj_list()
        ans = float('-inf')
        for i in range(n):
            visited = set()
            visited.add(i)
            dfs(i, visited, adj_list)
            ans = max(ans, len(visited))
        
        return ans


        