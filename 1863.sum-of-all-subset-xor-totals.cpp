// @leet start
#include <vector>
using std::vector;

class Solution {
public:

    int subsetXORSum(vector<int>& nums) {
        int n = nums.size();
        vector<int> xors = vector<int>(n);

        int sum = 0;
        for (int i = 0; i < n; ++i) {
            int xorvar =  nums[i] ^ xors[i-1];
            xors[i] = xorvar;
            sum += xorvar;
        }
        return sum;

    }

private:
};
// @leet end
