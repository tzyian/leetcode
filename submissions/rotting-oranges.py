// https://leetcode.com/problems/rotting-oranges

# multi-source bfs

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        nrow = len(grid)
        ncol = len(grid[0])

        queue = deque() 
        numfresh = 0 
        
        # save rotten and fresh oranges
        def find() -> int:
            nonlocal numfresh
            for rownum, row in enumerate(grid):
                for colnum, val in enumerate(row):
                    if val == 2:
                        queue.append((rownum, colnum))
                    elif val == 1:
                        numfresh += 1
            return

        def inside_grid(x: int, y: int) -> bool:
            return x >= 0 and x < nrow and y >= 0 and y < ncol

        def is_orange(x: int, y: int) -> bool:
            return grid[x][y] == 1 or grid[x][y] == 2

        #initialise sets
        find()

        # check edge cases
        if numfresh == 0:
            return 0
        elif len(queue) == 0:
            return -1

        #multi-source bfs (O(mn))
        visited: Set[Tuple[int, int]] = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ###             up      down    left     right

        time = 1

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                visited.add((x, y))

                for dx, dy in directions:
                    newx, newy = x + dx, y + dy
                    if not inside_grid(newx, newy):
                        continue

                    # if fresh, make rotten
                    if grid[newx][newy] == 1:
                        grid[newx][newy] = 2
                        numfresh -= 1

                    if is_orange(newx, newy) and (newx, newy) not in visited:
                        queue.append((newx, newy))

            if numfresh == 0:
                return time
            time +=1

        return -1


