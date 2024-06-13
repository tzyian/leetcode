// @leet start
#include <vector>
#include <unordered_map>
#include <algorithm>
using std::vector;


class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        // TC O(n + klogk), where k is leftover elements
        // SC O(n)
        std::unordered_map<int, int> hmap;
        for (const int& e : arr1) {
            ++hmap[e];
        }
        vector<int> ans;
        ans.reserve(arr1.size());
        for (const int& e : arr2) {
            while (hmap[e] > 0) {
                --hmap[e];
                ans.push_back(e);
            }
        }
        int sz = ans.size();
        for (auto it = hmap.begin(); it != hmap.end(); ++it) {
            while (it->second > 0) {
                --(it->second);
                ans.push_back(it->first);
            }
        }

        std::sort(ans.begin() + sz, ans.end());

        return ans;
        
    }
};
// @leet end
