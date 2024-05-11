// https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes

class Solution {
    fun findSmallestSetOfVertices(n: Int, edges: List<List<Int>>): List<Int> {
        val visited = BooleanArray(n)
        for (i in edges) {
            visited[i[1]] = true
        }
        val unvisited = mutableListOf<Int>()
        for ((index, value) in visited.withIndex()) {
            if (!value) {
                unvisited.add(index)
            }
        }
        return unvisited
    }
}