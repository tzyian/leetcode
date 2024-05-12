// @leet start
#include <vector>
using std::vector;

class Solution {
public:
    vector<vector<int>> largestLocal(vector<vector<int>> &grid) {
        int n = grid.size();
        int size = 3;
        vector<vector<int>> ans = vector<vector<int>>(n - 2, vector<int>(n - 2, 0));
        for (int i = 0; i < n - 2; i++) {
            for (int j = 0; j < n - 2; j++) {
                for (int k = 0; k < size; k++) {
                    for (int m = 0; m < size; m++) {
                        ans[i][j] = std::max(ans[i][j], grid[i + k][j + m]);
                    }
                }
            }
        }

        return ans;
    }
  
};
// @leet end
