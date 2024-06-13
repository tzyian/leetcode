// @leet start
#include <vector>
#include <unordered_map>
using std::vector;

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        // TC: O(n), SC: O(n)
        int total = 0;
        std::unordered_map<int, int> map;

        int prefixSum = 0;
        ++map[0];
        for (const int& ele : nums) {
            prefixSum += ele;
            total += map[prefixSum - k];
            ++map[prefixSum];
        }

        return total;
    }
};
// @leet end
