// @leet imports start

import java.util.*;
import java.math.*;
// @leet imports end

// @leet start
class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int ans = 0;
        int lowest = prices[0];
        for (int i = 1; i < n; i++) {
            ans = Math.max(ans, prices[i] - lowest);
            lowest = Math.min(lowest, prices[i]);
        }
        return ans;
    }
}
// @leet end
