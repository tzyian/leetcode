// @leet imports start

import java.util.*;
import java.math.*;
// @leet imports end

// @leet start
class Solution {
    public int candy(int[] ratings) {
        int n = ratings.length;
        int[] distrs = new int[n];
        Arrays.fill(distrs, 1);

        for (int i = 1; i < n; i++) {
            if (ratings[i] > ratings[i - 1]) {
                distrs[i] = distrs[i - 1] + 1;
            }
        }
        for (int i = n - 2; i >= 0; i--) {
            if (ratings[i] > ratings[i + 1]) {
                distrs[i] = Math.max(distrs[i], distrs[i + 1] + 1);
            }
        }
        return Arrays.stream(distrs).sum();
    }
}
// @leet end
