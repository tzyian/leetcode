// https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)
        grid = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(m + 1):
                if i == j == 0:
                    # both strings empty
                    # grid[0][0] already 0
                    continue
                elif i == 0:
                    # s1 empty, delete next s2
                    # s2[j - 1] because grid index = 1 + string index
                    grid[i][j] = grid[i][j - 1] + ord(s2[j - 1])
                elif j == 0:
                    # s2 empty, delete next s1
                    grid[i][j] = grid[i - 1][j] + ord(s1[i - 1])
                    
                elif s1[i - 1] == s2[j - 1]:
                    # same character, take the diagonal
                    grid[i][j] = grid[i - 1][j - 1]
                else:
                    # diff char, delete one
                    d1 = ord(s1[i - 1]) + grid[i - 1][j] # go down
                    d2 = ord(s2[j - 1]) + grid[i][j - 1] # go right
                    grid[i][j] = min(d1, d2)

        return grid[n][m]



