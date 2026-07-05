// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class Solution {
  public:
    int minScore(int n, vector<vector<int>>& roads) {
        uf.clear();
        min_score.clear();
        for (const auto& road : roads) {
            int a = road[0];
            int b = road[1];
            int dist = road[2];
            unite(a, b, dist);
        }
        int root = find(1);
        return min_score[root];
    }

  private:
    unordered_map<int, int> uf, min_score;
    int find(int x) {
        if (!uf.contains(x)) {
            uf[x] = x;
            min_score[x] = INT_MAX;
        }
        if (uf[x] != x) {
            uf[x] = find(uf[x]);
        }
        return uf[x];
    }
    void unite(int x, int y, int dist) {
        int px = find(x);
        int py = find(y);
        uf[px] = py;

        min_score[py] = min({dist, min_score[py], min_score[px]});
    }
};
// @leet end

class SolutionBfs {
  public:
    int minScore(int n, vector<vector<int>>& roads) {
        // since any edge and any town can be repeated,
        // find the connected component that connects node 1 to n
        // then find the minimum edge in this component

        unordered_map<int, unordered_map<int, int>> graph;
        for (const auto& road : roads) {
            int a = road[0];
            int b = road[1];
            int dist = road[2];
            graph[a][b] = dist;
            graph[b][a] = dist;
        }

        int min_score = INT_MAX;
        vector<int> stack{1};
        vector<int> visited(n + 1, 0);
        // NOTE: actually you don't even need to care about an edge being
        // visited only once max just which edges are reachable

        while (!stack.empty()) {
            auto curr = stack.back();
            stack.pop_back();
            // and we only count as visited once we expand all paths starting
            // from curr i.e. don't check visited within the for loop
            if (visited[curr]) {
                continue;
            }
            visited[curr] = 1;
            for (auto [nb, dist] : graph[curr]) {
                min_score = min(dist, min_score);
                stack.push_back(nb);
            }
        }
        return min_score;
    }
};

int main() {
    Solution s;
    int n = 4;
    vector<vector<int>> roads;
    int res;
    roads = {{1, 2, 9}, {2, 3, 6}, {2, 4, 5}, {1, 4, 7}};
    res = s.minScore(n, roads);
    debug(res);
    roads = {{1, 2, 2}, {1, 3, 4}, {3, 4, 7}};
    res = s.minScore(n, roads);
    debug(res);
}
