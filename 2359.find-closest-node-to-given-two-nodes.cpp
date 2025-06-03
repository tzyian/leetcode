#include <algorithm>
#include <climits>
#include <vector>
using std::vector;

// @leet start
class Solution {
  public:
    int closestMeetingNode(vector<int>& edges, int node1, int node2) {
        auto n = edges.size();
        auto dists1 = search(edges, node1);
        auto dists2 = search(edges, node2);
        int minimax = INT_MAX;
        int best_ind = -1;

        for (int i = 0; i < n; ++i) {
            if (dists1[i] == INT_MAX || dists2[i] == INT_MAX) {
                continue;
            }

            auto to_check = std::max(dists1[i], dists2[i]);
            if (to_check < minimax || (to_check == minimax && i < best_ind)) {
                minimax = to_check;
                best_ind = i;
            }
        }
        return best_ind;
    }

    vector<int> search(vector<int>& edges, int root) {
        auto n = edges.size();
        vector<int> visited(n);
        vector<int> dists(n, INT_MAX);
        int curr = root;

        int dist = 0;

        while (curr != -1 && !visited[curr]) {
            dists[curr] = dist++;
            visited[curr] = 1;
            curr = edges[curr];
        }
        return dists;
    }
};
// @leet end
