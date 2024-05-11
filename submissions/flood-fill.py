// https://leetcode.com/problems/flood-fill

from enum import Enum
class Direction(Enum):
    # R, C
    N = (-1, 0)
    S = (1, 0)
    E = (0, 1)
    W = (0, -1)


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = {}
        init_col = image[sr][sc]
        stack = []

        stack.append((sr, sc))
        image[sr][sc] = color
        visited[(sr, sc)] = True

        while len(stack) > 0:
            cur = stack.pop()
            for dir in Direction:
                newr = cur[0] + dir.value[0]
                newc = cur[1] + dir.value[1]
                if newr not in range(0, len(image)) or newc not in range(0, len(image[0])):
                    continue

                if (newr, newc) not in visited:
                    visited[(newr, newc)] = True
                    
                    if image[newr][newc] == init_col:
                        image[newr][newc] = color
                        stack.append((newr, newc))

        return image


            

        