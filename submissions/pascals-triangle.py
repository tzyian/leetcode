// https://leetcode.com/problems/pascals-triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows - 1
        ans = [[1]]
        for i in range(1, n+1):
            row = [1]
            for j in range(1, i):
                row.append(ans[i-1][j-1] + ans[i-1][j])
            row.append(1)
            ans.append(row)
        return ans
            

'''
0 1 2 3 4    
1           0
1 1         1
1 2 1       2
1 3 3 1     3
1 4 6 4 1   4


i = 2
for j in range(1,2):
    j = 1
    

'''