package leetcode

// O(log_b n) TC, where n is numBottles, b is numExchange
// func numWaterBottles(numBottles int, numExchange int) int {
// 	drank := numBottles
// 	for numBottles >= numExchange {
// 		drank += numBottles / numExchange
// 		numBottles = numBottles%numExchange + numBottles/numExchange
// 	}
// 	return drank
// }

// @leet start
// https://leetcode.com/problems/water-bottles/solutions/743148/java-python-3-o-logn-and-o-1-codes-w-brief-explanation-and-analysis/
// Assuming 9 bottles, and 3 old for 1 new
// The same old bottle can be used as the refill every time, but cannot be removed, hence numBottles-1
// numExchange-1 because 2 old are paid for 1 new
// O(1) TC, SC
func numWaterBottles(numBottles int, numExchange int) int {
	return numBottles + (numBottles-1)/(numExchange-1)
}

// @leet end
