// https://leetcode.com/problems/container-with-most-water

class Solution {
    public static int maxArea(int[] height) {
        int end = height.length - 1;
        int start = 0;
        int vol = 0;

        while (start < end) {
            int lower = Math.min(height[start], height[end]);
            int tmp = lower * (end - start);
            if (vol < tmp) {
                vol = tmp;
            }
            System.out.println(vol);
            if (height[start] > height[end]) {
                end--;
            } else if (height[start] < height[end]){
                start++;
            } else {
                start++;
                end--;
            }

        }
        return vol;
    }
}