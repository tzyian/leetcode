// https://leetcode.com/problems/is-graph-bipartite

class Solution {
    // array[index] is the nodes that index is adjacent to
    fun isBipartite(graph: Array<IntArray>): Boolean {

        val color = IntArray(graph.size)
        // 0 for unchecked, 1 for red, 2 for blue

        for (i in graph.indices) {
            if (color[i] != 0) {
                continue
            }

            val stack = ArrayDeque<Int>()
            stack.addLast(i)
            color[i] = 1

            while (!stack.isEmpty()) {
                val last: Int = stack.removeLast()
                for (adj in graph[last]) {
                    if (color[adj] == 0) {
                        color[adj] = -color[last]
                        stack.addLast(adj)
                    } else if (color[adj] == color[last]) {
                        return false
                    }
                }
            }
        }

        return true
    }
}