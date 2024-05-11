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

        image[sr][sc] = -1
        stack = [(sr, sc)]

        while stack:
            r, c = stack.pop()
            for dr, dc in directions:
                if not in_image(r + dr, c + dc):
                    continue
                elif image[r + dr][c + dc] == -1:
                    continue
                elif image[r + dr][c + dc] == orig:
                    image[r + dr][c + dc] = -1
                    stack.append((r + dr, c + dc))
        
        for i, row in enumerate(image):
            for j, _ in enumerate(row):
                if image[i][j] == -1:
                    image[i][j] = color

        return image    
