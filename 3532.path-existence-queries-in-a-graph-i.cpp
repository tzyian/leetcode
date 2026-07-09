// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class Solution {
  public:
    vector<bool> pathExistenceQueries(int n, vector<int>& nums, int maxDiff,
                                      vector<vector<int>>& queries) {
        // there's no need to use a std::map and --upper_bound() for this lol

        // TC O(n+q), SC O(n).
        int prev = nums[0];
        int curr_label = 0;
        vector<int> labels;
        labels.reserve(n);
        for (auto x : nums) {
            if (x - prev > maxDiff) {
                prev = x;
                labels.push_back(++curr_label);
            } else {
                prev = x;
                labels.push_back(curr_label);
            }
        }

        vector<bool> ans;
        ans.reserve(queries.size());
        for (const auto& q : queries) {
            ans.push_back(labels[q[0]] == labels[q[1]]);
        }
        return ans;
    }
};
// @leet end

int main() {
    Solution s;
    int n = 16;
    vector<int> nums = {8,  10, 11, 11, 21, 22, 23, 24,
                        28, 28, 29, 31, 33, 39, 50, 50};
    int maxDiff = 2;
    vector<vector<int>> queries = {
        {11, 4}, {1, 12}, {13, 13}, {6, 9},  {3, 9},   {7, 0},
        {1, 8},  {8, 7},  {1, 6},   {13, 4}, {15, 10}, {4, 3},
        {4, 9},  {3, 10}, {1, 3},   {15, 1}, {0, 6}};
    auto out = s.pathExistenceQueries(n, nums, maxDiff, queries);
    debug(out);
}
