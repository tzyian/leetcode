// https://leetcode.com/problems/search-in-rotated-sorted-array

/*
Double binary search:
identify point where the array is rotated using binary search
afterwards binary search in the appropriate range

Single binary search
https://leetcode.com/problems/search-in-rotated-sorted-array/solutions/154836/The-INF-and-INF-method-but-with-a-better-explanation-for-dummies-like-me/
 */

class Solution {
    fun search(nums: IntArray, target: Int): Int {
        var l = 0
        var r = nums.size - 1
        
        while (l < r) {
            val mid = l + (r - l) / 2
            var comparator = nums[mid]

            
            // qn constraint is all numbers distinct
            // Find pivot point (after the first loop, it is always nums[mid])
            if (((target < nums[0]) == (nums[mid] < nums[0]))) {
                comparator = nums[mid]
                // target and mid are on the same side of the pivot.
                // i.e. the range is sorted
                // Two possibilites:
                // 11 12 13 14 15 1 2 3 4 5
                // both true: mid = 15, target = 12
                // 11 12 13 14 15 1 2 3 4 5
                // both false: mid = 1, target = 3
                
            } else {
                // different side of the pivot i.e. not sorted in that range
                if (target < nums[0]) {
                    // search right side
                    // e.g. 12 13 14 15 1 2 3 4
                    // e.g. mid = 15, target = 3
                    comparator = Integer.MIN_VALUE
                } else {
                    // search left side
                    // e.g. 12 13 1 2 3 4 5
                    // e.g. mid = 2, target = 13
                    comparator = Integer.MAX_VALUE
                }
            }


            // regular binary search after the pivot index is found
            if (comparator >= target) {
                r = mid
            } else {
                l = mid + 1
            }
        }
        return if (nums[l] == target) l else -1

        // return -1
    }
}