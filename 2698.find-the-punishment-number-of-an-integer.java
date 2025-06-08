// @leet start

import java.util.HashMap;

class Solution {
    private static HashMap<Integer, Boolean> cache = new HashMap<>();

    private boolean is_valid(int num, int squared) {
        if (cache.containsKey(num)) {
            return cache.get(num);
        }
        String s = Integer.toString(squared);
        boolean res = canPartition(num, s, 0);
        cache.put(num, res);
        return res;
    }

    private boolean canPartition(int num, String s, int startIndex) {
        int n = s.length();
        if (num < 0) {
            return false;
        }

        if (startIndex == n) {
            return num == 0;
        }

        int val = 0;
        for (int i = startIndex; i < n; i++) {
            val = val * 10 + (s.charAt(i) - '0');
            boolean found = canPartition(num - val, s, i + 1);
            if (found) {
                return true;
            }
        }
        return false;

    }

    public int punishmentNumber(int n) {
        int ans = 0;
        for (int i = 1; i < n + 1; i++) {
            int squared = i * i;
            if (is_valid(i, squared)) {
                ans += squared;
            }
        }
        return ans;

    }
}
// @leet end
