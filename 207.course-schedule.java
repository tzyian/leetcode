// @leet start

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Deque;

class Solution {
    Deque<Integer> schedule;

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        this.schedule = new ArrayDeque<>();

        @SuppressWarnings("unchecked")
        List<Integer>[] adjList = new ArrayList[numCourses];

        for (int i = 0; i < numCourses; i++) {
            adjList[i] = new ArrayList<>();
        }

        for (int[] prereq : prerequisites) {
            adjList[prereq[1]].add(prereq[0]);
        }

        boolean[] visited = new boolean[numCourses];
        boolean[] recStack = new boolean[numCourses];

        for (int i = 0; i < numCourses; i++) {
            if (!visited[i]) {
                if (dfs(adjList, visited, recStack, i)) {
                    return false;
                }
            }
        }

        return true;
    }

    public boolean dfs(List<Integer>[] adjList, boolean[] visited, boolean[] recStack, int node) {
        if (recStack[node]) {
            return true;
        }
        if (visited[node]) {
            return false;
        }

        visited[node] = true;
        recStack[node] = true;

        for (Integer neighbor : adjList[node]) {
            if (dfs(adjList, visited, recStack, neighbor)) {
                return true;
            }
        }

        recStack[node] = false;
        schedule.addFirst(node);
        return false;
    }
}
// @leet end
