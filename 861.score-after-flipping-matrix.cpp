// @leet start
#include <cassert>
#include <iterator>
#include <sstream>
#include <vector>

using std::vector;

class Solution {
public:
    int matrixScore(vector<vector<int>>& grid) {
        replaceFirstCol(grid);
        replaceCols(grid);
        int score = countScore(grid);
        return score;

    }
private:
    void replaceFirstCol(vector<vector<int>>& grid) {
        int m = grid.size();
        for (int i = 0; i < m; i++) {
            if (grid[i][0] == 0) {
                flipRowBits(grid, i);
            }
        }

    }

    void flipRowBits(vector<vector<int>>& grid, int rowNum) {
        int n = grid[0].size();
        for (int j = 0; j < n; j++) {
            grid[rowNum][j] = grid[rowNum][j] == 0 ? 1 : 0;
        }

    }

    void replaceCols(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        for (int j = 1; j < m; j++) {
            int sum = 0;
            for (int i = 0; i < n; i++) {
                sum += grid[i][j];
            }
            if (sum <= n / 2) {
                flipColBits(grid, j);
            }
        }

    }

    void flipColBits(vector<vector<int>>& grid, int colNum) {
        int n = grid.size();
        for (int i = 0; i < n; i++) {
            grid[i][colNum] = grid[i][colNum] == 0 ? 1 : 0;
        }
    }

    int countScore(const vector<vector<int>>& grid) {
        int sum = 0;
        for (const auto& row : grid) {
            std::stringstream result;
            std::copy(row.begin(), row.end(), std::ostream_iterator<int>(result, ""));
            std::string res = result.str();
            sum += std::stoi(res, nullptr, 2);
        }
        return sum;

    }
};
// @leet end
