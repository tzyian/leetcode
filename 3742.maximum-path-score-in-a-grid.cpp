// @leet imports start
#include <bits/stdc++.h>
#include <vector>
using namespace std;
// @leet imports end

// @leet start
class Solution {
  public:
    int maxPathScore(vector<vector<int>>& grid, int k) {
        // this can be space optimised to nk or mk instead of mnk

        int m = grid.size();
        int n = grid[0].size();
        k = min(k, m + n - 2);

        // dp[i][j][c] = best points at (i, j) cell, at c cost
        auto dp = vector(m, vector(n, vector<int>(k + 2, -1)));

        dp[0][0][0] = 0;

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                for (int c = 0; c <= k; ++c) {
                    int cell = grid[i][j];
                    if (cell == 0) {
                        if (i > 0 && dp[i - 1][j][c] > -1) {
                            dp[i][j][c] = max(dp[i][j][c], dp[i - 1][j][c]);
                        }
                        if (j > 0 && dp[i][j - 1][c] > -1) {
                            dp[i][j][c] = max(dp[i][j][c], dp[i][j - 1][c]);
                        }
                    } else {
                        if (i > 0 && dp[i - 1][j][c] > -1) {
                            dp[i][j][c + 1] =
                                max(dp[i][j][c + 1], cell + dp[i - 1][j][c]);
                        }
                        if (j > 0 && dp[i][j - 1][c] > -1) {
                            dp[i][j][c + 1] =
                                max(dp[i][j][c + 1], cell + dp[i][j - 1][c]);
                        }
                    }
                }
            }
        }

        int ans = -1;
        for (int i = 0; i <= k; ++i) {
            ans = max(ans, dp[m - 1][n - 1][i]);
        }
        return ans;
    }
};
// @leet end

int main() {
    Solution s;
    vector<vector<int>> grid{{0, 1}, {2, 0}};
    int res = s.maxPathScore(grid, 1);
    std::cout << res;
}
