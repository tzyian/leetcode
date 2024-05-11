// https://leetcode.com/problems/top-k-frequent-elements

class Solution {
    fun topKFrequent(nums: IntArray, k: Int): IntArray {
        val freqTable = mutableMapOf<Int, Int>()
        for (num in nums) {
            freqTable[num] = freqTable.getOrDefault(num, 0) + 1
        }

        val numSet = freqTable.keys.toIntArray()
        quickSelect(numSet, 0, numSet.size - 1, k, freqTable)

        return numSet.copyOfRange(0, k)
    }

    private fun partition(ls: IntArray, start: Int, stop: Int, freq: Map<Int, Int>): Int {
        val pIndex = (start..stop).random()
        val pivot = freq[ls[pIndex]]!!
        swap(ls, start, pIndex)
        var low = start + 1
        var high = stop + 1
        while (low < high) {
            while (low < high && freq[ls[low]]!! >= pivot) {
                low++
            }
            while (low < high && (high > stop || freq[ls[high]]!! < pivot)) {
                high--
            }
            if (low < high) {
                swap(ls, low, high)
            }
        }
        swap(ls, start, low - 1)
        return low - 1

    }

    private fun swap(nums: IntArray, a: Int, b: Int) {
        val temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp
    }

    private fun quickSelect(numSet: IntArray, low: Int, high: Int, k: Int, freq: Map<Int, Int>) {
        val p = partition(numSet, low, high, freq)
        if (p == k - 1) {
            return
        }
        return if (p < k - 1) {
            quickSelect(numSet, p + 1, high, k, freq)
        } else {
            quickSelect(numSet, low, p - 1, k, freq)
        }
    }
}