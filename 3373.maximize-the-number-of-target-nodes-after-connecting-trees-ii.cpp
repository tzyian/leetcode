#include <algorithm>
#include <queue>
#include <unordered_set>
using std::unordered_set;
#include <vector>
using std::vector;
#include <unordered_map>
using std::unordered_map;

// @leet start
class Solution {
  public:
    static bool isOdd(int x) { return (x & 1) == 1; }
    static bool isEven(int x) { return (x & 1) == 0; }

    vector<int> maxTargetNodes(vector<vector<int>>& edges1,
                               vector<vector<int>>& edges2) {
        auto adj1 = constructAdjList(edges1);
        auto adj2 = constructAdjList(edges2);
        int n = adj1.size();
        int m = adj2.size();

        // colour tree1 into two groups (called odds and evens).
        // group1 nodes look at even nodes.
        // Likewise, colour tree2 into two groups. Whichever group has
        // more nodes can be joined to tree1

        auto colours1 = bfs(adj1, n);
        auto colours2 = bfs(adj2, m);

        auto odds1 = std::count_if(colours1.begin(), colours1.end(), isOdd);
        auto evens1 = std::count_if(colours1.begin(), colours1.end(), isEven);

        auto odds2 = std::count_if(colours2.begin(), colours2.end(), isOdd);
        auto evens2 = std::count_if(colours2.begin(), colours2.end(), isEven);
        auto best_tree2 = std::max(odds2, evens2);

        vector<int> res(n);
        for (int i = 0; i < n; ++i) {
            res[i] = (isOdd(colours1[i]) ? odds1 : evens1) + best_tree2;
        }
        return res;
    }

    vector<vector<int>> constructAdjList(vector<vector<int>>& edges) {
        vector<vector<int>> adj(edges.size() + 1);
        for (const auto& edge : edges) {
            int u = edge[0];
            int v = edge[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        return adj;
    }

    vector<int> bfs(vector<vector<int>>& adjList, int n) {
        // return the colour of every node
        unordered_set<int> visited;
        vector<int> colours(n);

        std::queue<int> queue;
        int root = 0;
        queue.push(0);
        visited.insert(0);

        int par = 0;

        while (!queue.empty()) {
            auto len = queue.size();
            for (auto i = 0; i < len; ++i) {
                int curr = queue.front();
                queue.pop();

                colours[curr] = par;

                for (auto nb : adjList[curr]) {
                    if (!visited.contains(nb)) {
                        visited.insert(nb);
                        queue.push(nb);
                    }
                }
            }
            par ^= 1;
        }

        return colours;
    }
};
// @leet end
