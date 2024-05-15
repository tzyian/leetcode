// @leet start
#include <vector>
#include <unordered_set>
#include <queue>
#include <utility>
#include <functional>
#include <algorithm>

using std::vector;
using std::unordered_set;
using std::pair;
using std::queue;
using std::priority_queue;

class Solution {
public:
    Solution() = default;

    int maximumSafenessFactor(vector<vector<int>>& grid) {
        this->n = grid.size();
        unordered_set<pair<int, int>, hash_pair> ones;
        getOnes(grid, ones); // generates vector of Ones
        msBfs(grid, ones); // generates grid of MH distance from closest One
        return dijkstra(grid);
    }

private:
    int n;
    vector<vector<int>> dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    
    struct hash_pair {
        template<class T1, class T2>
        size_t operator () (const pair<T1, T2> &pair) const {
            auto hash1 = std::hash<T1>{}(pair.first);
            auto hash2 = std::hash<T1>{}(pair.second);
            return hash1 ^ (hash2 << 1);
        }
        
    };

    void getOnes(const vector<vector<int>>& grid ,
                 unordered_set<pair<int, int>, hash_pair>& ones) const {
        for (int i = 0; i < this->n; ++i) {
            for (int j = 0; j < this->n; ++j) {
                if (grid[i][j] == 1) {
                    ones.emplace(i, j);
                }
            }
        }

    }
    void msBfs(vector<vector<int>>& grid, 
               const unordered_set<pair<int, int>, hash_pair>& ones) {

        queue<pair<int, int>> queue;
        for (const auto& coord : ones) {
            queue.push(coord);
        }

        unordered_set<pair<int, int>, hash_pair> visited(ones.begin(), ones.end());

        int levels = 0;

        while (!queue.empty()) {
            int sz = queue.size();
            for (int i = 0; i < sz; ++i) {
                const auto coord = queue.front();
                queue.pop();

                grid[coord.first][coord.second] = levels;

                for (const auto& dir : dirs) {
                    int newRow = coord.first + dir[0];
                    int newCol = coord.second + dir[1];

                    if (!isValidCell(grid, newRow, newCol)) {
                        continue;
                    }

                    const auto& newCoord = std::make_pair(newRow, newCol);

                    if (visited.insert(newCoord).second) {  
                        queue.push(newCoord);
                    }
                }
            }
            ++levels;
        }

    }

    bool isValidCell(const vector<vector<int>>& grid, int i, int j) const {
        return i >= 0 && i < n && j >= 0 && j < n;
    }

    int dijkstra(vector<vector<int>>& grid) const {
        // goal is minimax 
        // see 2040 rec9
        // taking a new edge is a min(a, b) function

        priority_queue<vector<int>> pq;

        pq.push(vector<int>{grid[0][0], 0, 0}); // safety factor, row, col
        grid[0][0] = -1;

        while (!pq.empty()) {
            const auto curr = pq.top();
            pq.pop();

            if (curr[1] == n - 1 && curr[2] == n - 1) {
                return curr[0];
            }

            for (auto& dir : dirs) {
                int newRow = dir[0] + curr[1];
                int newCol = dir[1] + curr[2];
                if (isValidCell(grid, newRow, newCol) && grid[newRow][newCol] != -1) {
                    pq.push(vector<int>{std::min(curr[0], grid[newRow][newCol]), newRow, newCol});
                    grid[newRow][newCol] = -1;
                }
            }
        }

        return -1; 
    }
};
// @leet end
