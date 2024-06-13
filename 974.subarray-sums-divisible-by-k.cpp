// @leet start

#include <unordered_map>
#include <vector>
using std::vector;

class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        // Concept similar to LC523.

        // TC O(n), SC O(k)
        std::unordered_map<int, int> map;
        int total = 0;
        int prefixSum = 0;

        ++map[0];

        for (const int& num : nums) {
            // Modulo because for 
            // prefixSum[i] % k == 4 and prefixSum[j] % k == 4, 
            // then the subarray between i and j fulfills condition
            prefixSum = (prefixSum + num) % k;

            if (prefixSum < 0) {
                // Deal with negative modulo issues
                prefixSum += k;
            }
            // No need to do [prefixSum - k] here because the % above does that
            total += map[prefixSum];
            ++map[prefixSum];
        }
        
        return total;
    }
};
// @leet end
