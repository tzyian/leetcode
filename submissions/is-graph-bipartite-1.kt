// https://leetcode.com/problems/is-graph-bipartite

// NOTE this solution is worse than the previously submitted one
class Solution {
    // array[index] is the nodes that index is adjacent to
    fun isBipartite(graph: Array<IntArray>): Boolean {
        val stack = ArrayDeque<Int>()
        // stack.addLast(0)
        // stack.removeLast()


        val checked = BooleanArray(graph.size)
        val color = IntArray(graph.size)
        // 0 for unchecked, 1 for red, 2 for blue

        // this loop is just to check for non-connected nodes
        for (i in graph.indices) {
            if (checked[i]) {
                continue
            }


            stack.addLast(i)
            if (color[i] == 0) color[i] = 1

            while (!stack.isEmpty()) {
                val last: Int = stack.removeLast()
                if (!checked[last]) {
                    checked[last] = true

                    for (i in graph[last]) {
                        if (color[last] == color[i]) return false
                        if (color[i] == 0) {
                            color[i] = -color[last]
                        }
                        if (!checked[i]) {
                            stack.addLast(i)
                        }
                    }

                }
            }
        }



        return true
    }
}