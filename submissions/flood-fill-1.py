// https://leetcode.com/problems/flood-fill


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
            for r, c in [(-1, 0), (1, 0), (0, 1), (0,-1)]:
                newr = cur[0] + r
                newc = cur[1] + c
                if not 0 <= newr < len(image) or not 0 <= newc < len(image[0]):
                    continue

                if (newr, newc) not in visited:
                    visited[(newr, newc)] = True
                    
                    if image[newr][newc] == init_col:
                        image[newr][newc] = color
                        stack.append((newr, newc))

        return image


            

        