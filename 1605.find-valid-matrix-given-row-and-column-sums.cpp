// @leet start
#include <climits>
#include <vector>
using std::vector;

class Solution {
public:
    vector<vector<int>> restoreMatrix(vector<int>& rowSum, vector<int>& colSum) {
        // TC O(mn), SC O(1)

        int numRows = rowSum.size();
        int numCols = colSum.size();

        vector<int> row(numCols); // zero initalisation
        vector<vector<int>> ans(numRows, row);
        // You can also do vec.resize(n) dynamically

        // Fill first column
        for (int i = 0; i < numRows; ++i) {
            ans[i][0] = rowSum[i];
        }

        // Move elements over to next columns
        // numCols - 1 because once the 2nd last col has been moved, guranteed valid
        // j is rowNum
        // i is colNum
        for (int i = 0; i < numCols - 1; ++i) {
            int colTotal = 0;

            for (int j = 0; j < numRows; ++j) {
                colTotal += ans[j][i];
                if (colTotal > colSum[i]) {
                    int diff = std::min(ans[j][i], colTotal - colSum[i]);
                    ans[j][i] -= diff;
                    ans[j][i + 1] = diff;
                    colTotal -= diff;
                }
            } 
        }

        return ans;
                                             
        
    }
};
// @leet end
