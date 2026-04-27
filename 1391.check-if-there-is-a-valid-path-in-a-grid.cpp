// @leet imports start
#include <bits/stdc++.h>
#include <vector>
using namespace std;
// @leet imports end

// @leet start
using Point = pair<int, int>;

class Solution {
  private:
    // Point LE = {0, -1};
    // Point RI = {0, 1};
    // Point UP = {-1, 0};
    // Point DO = {1, 0};
    enum DIRS { LEFT, RIGHT, UP, DOWN };
    map<DIRS, Point> dir_map = {
        {LEFT, {0, -1}},
        {RIGHT, {0, 1}},
        {UP, {-1, 0}},
        {DOWN, {1, 0}},
    };

    map<int, set<DIRS>> dirs = {
        {1, {LEFT, RIGHT}}, {2, {UP, DOWN}}, {3, {LEFT, DOWN}},
        {4, {RIGHT, DOWN}}, {5, {LEFT, UP}}, {6, {UP, RIGHT}},
    };

    map<DIRS, DIRS> opposite = {
        {LEFT, RIGHT}, {RIGHT, LEFT}, {UP, DOWN}, {DOWN, UP}};

  public:
    bool hasValidPath(vector<vector<int>>& grid) {
        vector<Point> stack = {{0, 0}};
        int n = grid.size();
        int m = grid[0].size();
        auto visited = vector(n, vector<int>(m));
        visited.push_back({0, 0});
        while (!stack.empty()) {
            auto [i, j] = stack.back();
            stack.pop_back();
            if (i == n - 1 && j == m - 1)
                return true;
            int cell = grid[i][j];
            auto nbs = dirs[cell];
            for (auto nb : nbs) {
                auto [di, dj] = dir_map[nb];
                int ni = i + di;
                int nj = j + dj;
                if (ni < 0 || ni >= n || nj < 0 || nj >= m)
                    continue;
                if (visited[ni][nj]) {
                    continue;
                }
                int next_cell = grid[ni][nj];
                const auto& next_cell_nbs = dirs[next_cell];
                DIRS opp = opposite[nb];
                if (!next_cell_nbs.contains(opp)) {
                    continue;
                }

                stack.push_back({ni, nj});
                visited[ni][nj] = 1;
            }
        }
        return false;
    }
};
// @leet end
