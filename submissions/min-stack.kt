// https://leetcode.com/problems/min-stack

// each min element needs to point to the next min

class MinStack() {
    private val stack: MutableList<Pair<Int, Int>> = mutableListOf()
    var minVal = Integer.MAX_VALUE

    fun push(`val`: Int) {
        stack.add(Pair(`val`, minVal))
        minVal = minVal.coerceAtMost(`val`)
    }

    fun pop() {
        val pair = stack.removeAt(stack.lastIndex)
        if (pair.first == minVal) {
            minVal = pair.second
        }
    }

    fun top(): Int {
        return stack[stack.lastIndex].first
    }

    fun getMin(): Int {
        return minVal
    }

}

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = MinStack()
 * obj.push(`val`)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */