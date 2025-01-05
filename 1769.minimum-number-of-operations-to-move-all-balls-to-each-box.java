// @leet start
class Solution {
    public int[] minOperations(String boxes) {
        int n = boxes.length();
        if (n == 0) {
            return new int[0];
        }

        int[] ans = new int[n];

        int pballs = boxes.charAt(0) - '0';
        int p_ops = 0;
        for (int i = 1; i < n; i++) {
            p_ops += pballs;
            ans[i] += p_ops;
            pballs += boxes.charAt(i) - '0';
        }

        int sballs = boxes.charAt(n - 1) - '0';
        int s_ops = 0;
        for (int i = n - 2; i >= 0; i--) {
            s_ops += sballs;
            ans[i] += s_ops;
            sballs += boxes.charAt(i) - '0';
        }

        return ans;
    }
}
// @leet end
