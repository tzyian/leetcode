// @leet start
#include <vector>
using std::vector;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        // []
        // [], add 1 to each
        // [] [1], add 2 to each
        // etc
        vector<vector<int>> ss;
        int n = nums.size();

        ss.push_back({});
        for (int i = 0; i < n; ++i) {
            // copy ss into s2
            vector<vector<int>> s2 = ss;

            for (auto& s : s2) {
                s.push_back(nums[i]);
                ss.insert(ss.end(), s);
            }
        }

        return ss;
        
    }
    
};

// @leet end
