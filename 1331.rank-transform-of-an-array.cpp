// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class Solution {
  public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        int n = arr.size();
        vector<int> indices(n, 0);
        std::iota(indices.begin(), indices.end(), 0);
        std::sort(indices.begin(), indices.end(),
                  [&](int i, int j) { return arr[i] < arr[j]; });
        vector<int> ans(n, 1);
        // arr[i] = 4, 1, 2, 3
        // sorted = 1, 2, 3, 4
        // sorted inx = 2, 3, 4, 1
        for (int i = 1; i < n; ++i) {
            if (arr[indices[i]] == arr[indices[i - 1]]) {
                ans[indices[i]] = ans[indices[i - 1]];
            } else {
                ans[indices[i]] = ans[indices[i - 1]] + 1;
            }
        }

        return ans;
    }
};
// @leet end
