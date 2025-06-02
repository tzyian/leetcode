// @leet start

import java.util.HashMap;
import java.util.PriorityQueue;

class Solution {
    // adapted from
    // https://leetcode.com/problems/cheapest-flights-within-k-stops/solutions/267200/python-dijkstra/
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        // Adj list
        HashMap<Integer, HashMap<Integer, Integer>> graph = new HashMap<>();
        for (int[] flight : flights) {
            int s = flight[0];
            int d = flight[1];
            int price = flight[2];
            graph.putIfAbsent(s, new HashMap<>());
            graph.get(s).put(d, price);
        }

        // Dijkstra
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        int[] start = { 0, src, k + 1 }; // {cost, node, depth left}
        pq.offer(start);

        // Visited records the remaining steps available on reaching node i at the
        // lowest cost
        // If vis[i] >= k, skip visiting because we already found a cheaper way to this
        // node
        int[] visited = new int[n];

        while (!pq.isEmpty()) {
            int[] current = pq.poll();
            int cost = current[0];
            int node = current[1];
            int stops = current[2];

            if (node == dst) {
                return cost;
            }
            // Skip if we already found a way here with fewer stops
            // Since on pq.poll(), we know it is the cheapest cost to reach this node with
            // this cost
            if (visited[node] >= stops) {
                continue;
            }
            visited[node] = stops;

            if (stops > 0) {
                HashMap<Integer, Integer> neighbours = graph.getOrDefault(node, new HashMap<>());
                for (int nb : neighbours.keySet()) {
                    int edge = neighbours.get(nb);

                    pq.offer(new int[] {
                            cost + edge, nb, stops - 1
                    });
                }
            }
        }
        return -1;
    }
}
// @leet end
