// https://leetcode.com/problems/two-sum

class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val set = mutableMapOf<Int, Int>()
                
        for ((index, value) in nums.withIndex()) {
            set[value] = index
        }

        for ((index, value) in nums.withIndex()) {
            val complement = target - value
            if (set.containsKey(complement) && set[complement] != index) {
                return intArrayOf(index, set[complement]!!)
            }
        }
        return intArrayOf(0, 0)
    }
}