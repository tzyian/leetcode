// @leet start
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>
using namespace std;

class Solution {
public:
    string largestNumber(vector<int>& nums) {
        std::sort(nums.begin(), nums.end(), [](int a, int b) {
            string sa = to_string(a);
            string sb = to_string(b);
            return sa + sb > sb + sa;
        });
        return nums[0] == 0 ? "0" : accumulate(nums.begin(), nums.end(), string(), [](const string& a, int b) {
            return a + to_string(b);
        });
    }
};
// @leet end
