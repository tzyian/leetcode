// https://leetcode.com/problems/number-of-provinces

# adj matrix

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs1(index, visited, stack, graph):
            for to in range(len(graph[index])):
                if graph[index][to] == 1 and to not in visited:
                    visited.add(to)
                    dfs1(to, visited, stack, graph)
            stack.append(index)


        def dfs2(newgraph, stack) -> list[list]:
            numcomponent = 0
            visited = set()
            while stack:
                index = stack.pop()
                if index not in visited:
                    visited.add(index)
                    dfs1(index, visited, [], newgraph)
                    numcomponent += 1
            return numcomponent
        



        graph = isConnected
        if not graph:
            return [[]]
        visited = set()
        stack = []
        for i in range(len(graph)):
            if i not in visited:
                dfs1(i, visited, stack, graph)
        return dfs2(graph, stack)


