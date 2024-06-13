// @leet start
#include <vector>
#include <unordered_map>
using std::vector;

class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        // See LC974
        //
        // TC O(n), SC O(k)
        std::unordered_map<int, int> map;

        int prefixSum = 0;
        int prevSum = 0;

        // Don't do ++map[0] here because 
        // you do it in first iteration prevSum
        for (const int& num : nums) {
            prefixSum = (prefixSum + num) % k;
            if (map[prefixSum] > 0) {
                return true;
            }
            ++map[prevSum];
            prevSum = prefixSum;
        }
        return false;
    }
};
// @leet end
