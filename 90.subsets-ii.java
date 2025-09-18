
// @leet imports start
import java.util.*;
import java.math.*;
// @leet imports end

// @leet start
class Solution {
    List<List<Integer>> ans;
    int[] nums;

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        this.ans = new ArrayList<>();
        this.nums = nums;

        List<Integer> curr = new ArrayList<>();
        Arrays.sort(nums);
        dfs(0, curr);
        return ans;

    }

    private void dfs(int start, List<Integer> curr) {
        List<Integer> copy = new ArrayList<>(curr);
        ans.add(copy);

        for (int i = start; i < nums.length; i++) {
            if (i > start && nums[i] == nums[i - 1]) {
                continue;
            }
            curr.add(nums[i]);
            dfs(i + 1, curr);
            curr.removeLast();
        }
    }
}
// @leet end
