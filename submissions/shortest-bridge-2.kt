// https://leetcode.com/problems/shortest-bridge


import java.lang.IllegalArgumentException
import java.util.*


/* Find first island using BFS/DFS
 * Then multi-source BFS to find 2nd island
 */

class Solution {
    enum class Direction(val dx: Int, val dy: Int) {
        NORTH(0, 1),
        SOUTH(0, -1),
        EAST(1, 0),
        WEST(-1, 0)
    }

    private fun firstIsland(grid: Array<IntArray>): Pair<Int, Int> {
        for (r in grid.indices) {
            for (c in grid[0].indices) {
                if (grid[r][c] == 1) {
                    return Pair(r, c)
                }
            }
        }
        throw IllegalArgumentException("no islands found")
    }

    private fun firstIslandCoords(grid: Array<IntArray>): Set<Pair<Int, Int>> {
        // Locate a starting point of Island 1
        val initial = firstIsland(grid)
        println(initial)

        // DFS to find all coord of island 1
        val island1Coords = mutableSetOf<Pair<Int, Int>>()
        val visited: Array<BooleanArray> = Array(grid.size) { BooleanArray(grid[0].size) }
        val stack: Stack<Pair<Int, Int>> = Stack()

        stack.push(initial)
        while (stack.isNotEmpty()) {
            val coord = stack.pop()
            visited[coord.first][coord.second] = true
            if (grid[coord.first][coord.second] == 0) {
                continue
            }
            island1Coords.add(Pair(coord.first, coord.second))

            for (dir in Direction.values()) {
                val x = coord.first + dir.dx
                val y = coord.second + dir.dy
                if (x !in grid.indices || y !in grid[0].indices) {
                    continue
                }
                if (!visited[x][y]) {
                    stack.add(Pair(x, y))
                }
            }
        }
        return island1Coords
    }


    fun shortestBridge(grid: Array<IntArray>): Int {
        val island1: Set<Pair<Int, Int>> = firstIslandCoords(grid)
        println(island1)
        // val island1 is all the coordinates of Island1



        // BFS to find number of 0s need to flip to find another 1
        val queue: Queue<Pair<Int, Int>> = LinkedList()
        queue.addAll(island1)
        val innerQueue: Queue<Pair<Int, Int>> = LinkedList()
        val visited: Array<BooleanArray> = Array(grid.size) { BooleanArray(grid[0].size) }
        var counter = 0

        while (!queue.isEmpty()) {
            val coord: Pair<Int, Int> = queue.poll()

            for (dir in Direction.values()) {
                val x = coord.first + dir.dx
                val y = coord.second + dir.dy
                if (x !in grid.indices || y !in grid[0].indices || Pair(x,y) in island1) {
                    continue
                }
                if (grid[x][y] == 1) {
                    return counter
                }
                if (!visited[x][y]) {
                    visited[x][y] = true
                    innerQueue.add(Pair(x, y))
                }
            }

            if (queue.isEmpty()) {
                counter++
                queue.addAll(innerQueue)
            }
        }
        return -1

    }
}