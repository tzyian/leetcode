
// @leet imports start
import java.util.*;
import java.math.*;
// @leet imports end

// @leet start

class Solution {
    private record Pair(int val, int idx) {
    }

    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        int[] ans = new int[n - k + 1];
        PriorityQueue<Pair> pq = new PriorityQueue<>((a, b) -> Integer.compare(b.val(), a.val()));

        for (int i = 0; i < n; i++) {
            Pair p = new Pair(nums[i], i);
            pq.add(p);

            if (i - k + 1 < 0) {
                continue;
            }

            while (!pq.isEmpty() && pq.peek().idx() < i - k + 1) {
                pq.poll();
            }

            ans[i - k + 1] = pq.peek().val();
        }

        return ans;

    }
}
// @leet end
