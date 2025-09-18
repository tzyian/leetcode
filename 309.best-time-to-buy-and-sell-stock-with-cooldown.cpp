#include <climits>
#include <vector>
using std::vector;

// @leet start
class Solution {
  public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int canBuy = 0;
        int canSell = -prices[0];
        int mustRest = INT_MIN;

        for (int i = 1; i < n; ++i) {
            // honestly, just make 3 temporary variables to avoid needing to
            // reorder things
            int tempRest = mustRest;
            mustRest = canSell + prices[i];
            canSell = std::max(canBuy - prices[i], canSell);
            canBuy = std::max(canBuy, tempRest);
        }
        return std::max(canBuy, mustRest);
    }

    // int maxProfit(vector<int>& prices) {
    //     int n = prices.size();
    //     vector<int> canBuy(n);
    //     vector<int> canSell(n);
    //     vector<int> mustRest(n);
    //     canBuy[0] = 0;
    //     canSell[0] = -prices[0];
    //     mustRest[0] = INT_MIN;
    //
    //     for (int i = 1; i < n; ++i) {
    //         canBuy[i] = std::max(canBuy[i - 1], mustRest[i - 1]);
    //         canSell[i] = std::max(canBuy[i - 1] - prices[i], canSell[i - 1]);
    //         mustRest[i] = canSell[i - 1] + prices[i];
    //     }
    //     return std::max(canBuy[n - 1], mustRest[n - 1]);
    // }
};
// @leet end
