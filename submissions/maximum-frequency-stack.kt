// https://leetcode.com/problems/maximum-frequency-stack

class FreqStack() {
    // map of number to frequency. Freq tells you which level to put it on the stack
    private val freqTable = mutableMapOf<Int, Int>()

    // map of frequency to stack<number>
    private val stackLevels = mutableMapOf<Int, Stack<Int>>()

    // tells you which is the maximum level to pop off
    private var maxFreq = 0


    fun push(`val`: Int) {
//        val pushFreq = freqTable.getOrPut(`val`) { 1 }
//        val pushFreq = freqTable.getOrPut(`val`) { 1 }
////      note this particular getOrPut above doesn't increment if val is already inside
    val pushFreq: Int = freqTable.getOrDefault(`val`, 0) + 1
    freqTable[`val`] = pushFreq
    maxFreq = maxFreq.coerceAtLeast(pushFreq)
    stackLevels
        .computeIfAbsent(pushFreq) { Stack() }
        .push(`val`)
    }

    fun pop(): Int {
        val popNumber = stackLevels
            .getOrElse(maxFreq) { throw IndexOutOfBoundsException() }
            .pop()
        freqTable.merge(popNumber, 0) { old, _ -> old - 1 } // reduce freq of ele by 1
        if (stackLevels[maxFreq]?.isEmpty() == true) {
            maxFreq--
        }
        return popNumber
    }

}

/**
 * Your FreqStack object will be instantiated and called as such:
 * var obj = FreqStack()
 * obj.push(`val`)
 * var param_2 = obj.pop()
 */