// https://leetcode.com/problems/shortest-path-in-binary-matrix

from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        nrow = ncol = len(grid)
        if grid[0][0] == 1 or grid[nrow - 1][ncol - 1] == 1:
            return -1
        if nrow == 1:
            return 1


        dir = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == j and i == 0:
                    continue
                dir.append((i, j))

        visited = set()

        q = deque()
        q.append((0,0))
        visited.add((0,0))
        dist = 1 # 0 hops = 1 cell
        while q:
            size = len(q)
            for _ in range(0, size): # this is the line so u dont have to make another q
                r, c = q.popleft()
                if r == nrow - 1 and c == ncol - 1:
                    return dist
                for dr, dc in dir:
                    newr = r + dr
                    newc = c + dc
                    if newr < 0 or newr >= nrow or newc < 0 or newc >= ncol \
                            or grid[newr][newc] != 0:
                        continue
                    if (newr, newc) not in visited:
                        visited.add((newr, newc))
                        q.append((newr, newc))
            dist += 1
            
        
        return -1
            
                




        
        