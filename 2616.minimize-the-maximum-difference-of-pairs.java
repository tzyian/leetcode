// @leet start

import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int minimizeMax(int[] nums, int p) {
        // NOTE: this doesn't work.
        // Checking (0, 1), (2, 3), (4, 5) etc
        // will always be better or equal
        // to checking (1, 2), (3, 4), (5, 6) and so on.
        int n = nums.length;

        if (p == 0 || n < 2) {
            return 0;
        }

        Arrays.sort(nums);
        ArrayList<Integer> odds = new ArrayList<>();
        ArrayList<Integer> evens = new ArrayList<>();

        // 0 1 2 3 4
        for (int i = 1; i < n; i++) {
            if (i % 2 == 1) {
                odds.add(Math.abs(nums[i] - nums[i - 1]));
            } else {
                evens.add(Math.abs(nums[i] - nums[i - 1]));
            }
        }
        int[] oddsArr = odds.stream().mapToInt(i -> i).toArray();
        int[] evensArr = evens.stream().mapToInt(i -> i).toArray();
        Arrays.sort(oddsArr);
        Arrays.sort(evensArr);

        System.out.println(Arrays.toString(nums));
        System.out.println(Arrays.toString(oddsArr));
        System.out.println(Arrays.toString(evensArr));

        int min = Integer.MAX_VALUE;
        if (oddsArr.length >= p) {
            min = Math.min(min, oddsArr[p - 1]);
        }
        if (evensArr.length >= p) {
            min = Math.min(min, evensArr[p - 1]);
        }
        return min;

    }
}
// @leet end

// [3,0,5,0,0,1,6]
// [0,0,0,1,3,5,6]
// [ 0 0 1 2 2 1]
// [ 0 0 1 1 2 2]
