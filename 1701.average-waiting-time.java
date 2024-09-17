// @leet start
class Solution {
    public double averageWaitingTime(int[][] customers) {
        // Beware integer overflow
        double totalTime = 0;
        double numCust = customers.length;
        double currTime = 0;

        for (int i = 0; i < numCust; i++) {
            int arrivalTime = customers[i][0];
            int prepTime = customers[i][1];

            if (arrivalTime < currTime) {
                // waiting for prev to finish
                totalTime += currTime - arrivalTime;
            } else {
                currTime = arrivalTime;
            }
            totalTime += prepTime;
            currTime += prepTime;
        }

        return totalTime / numCust;
    }
}
// @leet end
