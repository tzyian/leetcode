// @leet start
#include <vector>
using std::vector;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int best = 0;
        int lo = 0;
        int hi = 1;
        int n = prices.size();
        
        while (hi < n) {
            if (prices[hi] <= prices[lo]) {
                lo = hi;
            }
            best = std::max(prices[hi] - prices[lo], best);
            ++hi;
        }

        return best;
    }
};
// @leet end
