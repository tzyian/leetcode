// @leet start
#include <vector>
#include <utility>
using std::vector;

class Solution {
public:
    Solution(): n(0), m(0), gridPtr(nullptr) {};
    int getMaximumGold(vector<vector<int>>& grid) {
        this->n = grid.size();
        this->m = grid[0].size();
        this->gridPtr = &grid;


        int best = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] != 0) {
                    int newVal = goldBacktrack(i, j);
                    best = std::max(best, newVal);
                }
            }
        }
        return best;


    }
private:
    int n;
    int m;
    vector<vector<int>>* gridPtr;

    int goldBacktrack(int row, int col) {
        vector<vector<int>>& grid = *(this->gridPtr);
        if (row < 0 || row >= n || col < 0 || col >= m || grid[row][col] == 0) {
            return 0;
        }
        int saved = grid[row][col];
        grid[row][col] = 0;

        int best = 0;
        vector<std::pair<int, int>> dirs = {{-1, 0}, {1, 0},{0, -1},{0, 1}};
        for (const auto& dir : dirs) {
            best = std::max(best, goldBacktrack(row + dir.first, col + dir.second));
        }
        

        grid[row][col] = saved;

        return best + saved;
    }
};
// @leet end
