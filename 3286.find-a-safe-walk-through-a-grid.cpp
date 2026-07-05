// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class Solution {
  public:
    bool findSafeWalk(vector<vector<int>>& grid, int health) {
        // This solution uses bfs with visited to check every point
        // Dijkstra can be used to check shortest path to End < Heatlh
        // 0-1 BFS
        using pii = pair<int, int>;
        using tpl = tuple<int, int, int>;

        int n = grid.size();
        int m = grid[0].size();

        if (grid[0][0] == 1) {
            --health;
        }

        vector<pii> dirs = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
        vector<tpl> stack{{0, 0, health}};
        auto visited = vector(n, vector(m, 0));
        visited[0][0] = health;

        auto is_valid = [=](int i, int j) {
            bool in_grid = 0 <= i && i < n && 0 <= j && j < m;
            return in_grid;
        };
        while (!stack.empty()) {
            auto [i, j, curr_hp] = stack.back();
            if (i == n - 1 && j == m - 1 && curr_hp > 0) {
                return true;
            }
            stack.pop_back();
            for (auto [di, dj] : dirs) {
                int ni = i + di;
                int nj = j + dj;
                if (is_valid(ni, nj)) {
                    if (grid[ni][nj] == 0 && curr_hp > visited[ni][nj]) {
                        stack.emplace_back(ni, nj, curr_hp);
                        visited[ni][nj] = curr_hp;
                    } else if (grid[ni][nj] == 1 && curr_hp > 1 &&
                               curr_hp - 1 > visited[ni][nj]) {
                        stack.emplace_back(ni, nj, curr_hp - 1);
                        visited[ni][nj] = curr_hp - 1;
                    }
                }
            }
        }

        return false;
    }
};
// @leet end
