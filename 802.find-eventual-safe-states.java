// @leet start

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public List<Integer> eventualSafeNodes(int[][] graph) {
        // adapted from NeetCode

        int n = graph.length;
        Map<Integer, Boolean> isSafe = new HashMap<>();
        ArrayList<Integer> ans = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (this.dfs(i, isSafe, graph)) {
                ans.add(i);
            }
        }
        return ans;

    }

    boolean dfs(int i, Map<Integer, Boolean> isSafe, int[][] graph) {
        if (isSafe.containsKey(i)) {
            return isSafe.get(i);
        }
        isSafe.put(i, false);

        for (int nb : graph[i]) {
            if (!dfs(nb, isSafe, graph)) {
                return false;
            }

        }
        isSafe.put(i, true);
        return true;

    }
}
// @leet end
