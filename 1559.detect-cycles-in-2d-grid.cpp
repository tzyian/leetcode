// @leet imports start
#include <bits/stdc++.h>
#include <utility>
using namespace std;
// @leet imports end

// @leet start
using State = std::array<int, 4>;

struct Coord {
    int y, x;
    bool operator==(const Coord& other) const {
        return y == other.y && x == other.x;
    }
    struct HashFunction {
        size_t operator()(const Coord& c) const {
            return std::hash<int>()(c.y) ^ (std::hash<int>()(c.x) << 1);
        }
    };
};

// a cycle of length >= 4 in a grid just means meeting a visited node again

class Solution {
  private:
    vector<pair<int, int>> dirs = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};

  public:
    bool containsCycle(vector<vector<char>>& grid) {
        // can use a vec<vec<int>> here rather than writing hash
        unordered_set<Coord, Coord::HashFunction> visited;
        int n = grid.size();
        int m = grid[0].size();

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (visited.contains({i, j})) {
                    continue;
                }

                vector<State> stack = {{i, j, -1, -1}};
                visited.emplace(i, j);
                // dfs here
                while (!stack.empty()) {
                    const auto [y, x, py, px] = stack.back();
                    stack.pop_back();
                    for (const auto [dy, dx] : dirs) {
                        int ny = y + dy;
                        int nx = x + dx;
                        if (ny < 0 || ny >= n || nx < 0 || nx >= m)
                            continue;
                        if (grid[y][x] != grid[ny][nx])
                            continue;
                        if (ny == py && nx == px)
                            continue;
                        if (visited.contains({ny, nx}))
                            return true;

                        visited.emplace(ny, nx);
                        stack.push_back({ny, nx, y, x});
                    }
                }
            }
        }
        return false;
    }
};
// @leet end

int main() {
    Solution s;
    vector<vector<char>> grid = {{'a', 'a', 'a', 'a'},
                                 {'a', 'b', 'b', 'a'},
                                 {'a', 'b', 'b', 'a'},
                                 {'a', 'a', 'a', 'a'}};
    // bool x = s.containsCycle(grid);
    // printf("%d\n", x);
    vector<vector<char>> grid2 = {
        {'a', 'b', 'b'},
        {'b', 'z', 'b'},
        {'b', 'b', 'a'},
    };
    bool x = s.containsCycle(grid2);
    printf("%d\n", x);
}
