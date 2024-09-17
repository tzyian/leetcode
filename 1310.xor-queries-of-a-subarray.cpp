// @leet start
#include <numeric>
#include <vector>
using std::vector;

class Solution {
  public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        vector<int> prefix_xors(arr.size());
        std::partial_sum(arr.cbegin(), arr.cend(), prefix_xors.begin(),
                         std::bit_xor());

        vector<int> ans(queries.size());

        for (int i = 0; i < queries.size(); i++) {
            int start = queries[i][0];
            int end = queries[i][1];
            if (start == 0) {
                ans[i] = prefix_xors[end];
            } else {
                ans[i] = prefix_xors[end] ^ prefix_xors[start - 1];
            }
        }

        return ans;
    }
};
// @leet end
