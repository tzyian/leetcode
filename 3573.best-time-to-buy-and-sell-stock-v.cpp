// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class Solution {
    using ll = long long;

  private:
    vector<int> prices;
    vector<vector<vector<ll>>> memo;

    static constexpr int NOT_HOLDING = 0;
    static constexpr int HOLDING = 1;
    static constexpr int SHORT_SELL = 2;
    static constexpr ll NEG_INF = LLONG_MIN / 4;

    ll dp(int i, int k_left, int state, bool can_ss) {
        if (i == prices.size() || k_left == 0) {
            if (state == NOT_HOLDING)
                return 0;
            else
                return NEG_INF;
        }
        ll& ans = memo[i][k_left][state];
        if (ans != -1)
            return ans;

        if (state == NOT_HOLDING) {
            ll buy = -prices[i] + dp(i + 1, k_left, HOLDING, can_ss);
            if (can_ss) {
                ll shortsell =
                    prices[i] + dp(i + 1, k_left, SHORT_SELL, can_ss);
                ans = max(buy, shortsell);
            } else {
                ans = buy;
            }
        } else if (state == HOLDING) {
            ll sell = prices[i] + dp(i + 1, k_left - 1, NOT_HOLDING, can_ss);
            ans = sell;
        } else {
            // SHORT_SELL
            ll buy_back =
                -prices[i] + dp(i + 1, k_left - 1, NOT_HOLDING, can_ss);
            ans = buy_back;
        }
        ll skip = dp(i + 1, k_left, state, can_ss);
        ans = max(ans, skip);
        return ans;
    }

  public:
    long long maximumProfit(vector<int>& prices, int k) {
        this->prices = prices;
        memo.assign(prices.size(), vector(k + 1, vector<ll>(3, -1)));
        return dp(0, k, NOT_HOLDING, true);
    }
};
;
// @leet end

int main() {}
