// https://leetcode.com/problems/flood-fill

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        nr = len(image)
        nc = len(image[0])

        def in_image(r, c):
            return 0 <= r and r < nr and 0 <= c and c < nc

        orig = image[sr][sc]
        directions = (-1, 0), (1, 0), (0, -1), (0, 1)
        ###             up      down   left     right

        image[sr][sc] = color
        stack = [(sr, sc)]

        visited = set()
        visited.add((sr, sc))

        while stack:
            r, c = stack.pop()
            print(r, c)
            for dr, dc in directions:
                if not in_image(r + dr, c + dc) or (r + dr, c + dc) in visited:
                    continue
                elif image[r + dr][c + dc] == orig:
                    image[r + dr][c + dc] = color
                    stack.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))

        return image    
