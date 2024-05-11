// https://leetcode.com/problems/top-k-frequent-elements

class Solution {
    /* Solution:
     * Iterate once through to make a hashmap of frequency
     * Quickselect the kth smallest item
     * return the array
     */
    fun topKFrequent(nums: IntArray, k: Int): IntArray {
        val freqTable = mutableMapOf<Int, Int>()
        for (i in nums) {
            freqTable[i] = freqTable.getOrDefault(i, 0) + 1
            // freqTable.getOrPut(i) { 0 } + 1
            //      kotlin method. get(i), if not calls the lambda, puts the result into the map
            //      then get(i)
            // freqTable.getOrElse(i) { 0 } + 1
            //      kotlin method. get(i), else call the lambda
            // freqTable[i]]?.plus(1) ?: 1
            //      using elvis operator
            // freqTable.getOrDefault(i, 0) + 1
            //      java map method, same as getOrElse but with diff method signature
        }
        val heap = PriorityQueue<Int>(k){x,y -> freqTable[y]!! - freqTable[x]!! }
        // if you want min at the top, you use x - y
        // if you want max at the top, you use y - x
        // val heap2 = PriorityQueue<Int>(Comparator.comparingInt<Int> { freqTable[it]!! }.reversed())
        //      is another way to do max at the top
        for (num in freqTable.keys) {
            heap.add(num)
        }
        val result = IntArray(k)
        for ((index, i) in (0 until k).withIndex()) {
            result[index] = heap.poll()
        }
        return result

    }
}