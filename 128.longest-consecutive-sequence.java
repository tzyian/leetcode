
// @leet imports start
import java.util.*;
import java.math.*;
// @leet imports end

// @leet start
class Solution {
    public int longestConsecutive(int[] nums) {
        Map<Integer, Integer> m = new HashMap<>();
        int ans = 0;
        for (int i : nums) {
            if (!m.containsKey(i)) {
                // connect m[i] to m[i+1] and m[i-1]
                int less = m.getOrDefault(i - 1, 0);
                int more = m.getOrDefault(i + 1, 0);
                int curr = less + more + 1;
                m.put(i, curr);
                // update the boundary values
                if (less > 0) {
                    m.put(i - less, curr);
                }
                if (more > 0) {
                    m.put(i + more, curr);
                }
                ans = Math.max(ans, curr);
            }
        }
        return ans;

    }
}
// @leet end
