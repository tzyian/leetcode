// https://leetcode.com/problems/evaluate-division

class Solution {
    /*
    Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000
     */


    fun calcEquation(equations: List<List<String>>, values: DoubleArray, queries: List<List<String>>): DoubleArray {
        // construct graph
        val graph: MutableMap<String, MutableMap<String, Double>> = mutableMapOf()
        for (i in values.indices) {
            if (graph[equations[i][0]] == null) {
                graph[equations[i][0]] = mutableMapOf()
            }
            if (graph[equations[i][1]] == null) {
                graph[equations[i][1]] = mutableMapOf()
            }
            graph[equations[i][0]]?.put(equations[i][1], values[i])
            graph[equations[i][1]]?.put(equations[i][0], 1 / values[i])
        }

//        val x = graph.toString()
//        println(x)

        // DFS queries
        val result = DoubleArray(queries.size)

        for (ind in queries.indices) {
            val firstVar: String = queries[ind][0]
            val secondVar: String = queries[ind][1]
            val value = dfs(graph, firstVar, secondVar, mutableSetOf())
            result[ind] = value
        }

        return result
    }


    private fun dfs(graph: MutableMap<String, MutableMap<String, Double>>, firstVar: String, secondVar: String, checked: MutableSet<String>): Double {
        if (firstVar !in graph || secondVar !in graph || graph[firstVar] == null) {
            return -1.0
        } else if (graph[firstVar]?.contains(secondVar) == true) {
            return graph[firstVar]?.get(secondVar)!!
        } else if (firstVar == secondVar) {
            return 1.0
        }
        for (str in graph[firstVar]!!.keys) {
            if (str !in checked) {
                checked.add(str)
                val check = dfs(graph, str, secondVar, checked)
                if (check != -1.0) {
                    return graph[firstVar]?.get(str)!! * check
                }
            }
        }

        return -1.0
    }

}