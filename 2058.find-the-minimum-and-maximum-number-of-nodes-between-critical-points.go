package leetcode

// @leet start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func nodesBetweenCriticalPoints(head *ListNode) []int {
	// SC O(1), TC O(n) single pass
	// Note question asks for max between *any* two critical points i.e. first and last

	firstCriticalIndex := -1
	lastCriticalIndex := -1

	minDistance := 1_000_000

	distSinceLast := -1

	// Start at node index 1
	prevVal := head.Val
	curr := head.Next
	index := 1

	for curr.Next != nil {
		isLMax := prevVal < curr.Val && curr.Val > curr.Next.Val
		isLMin := prevVal > curr.Val && curr.Val < curr.Next.Val

		if isLMax || isLMin {
			if firstCriticalIndex == -1 {
				firstCriticalIndex = index
			} else {
				// ensure there is at least 1 critical point first
				lastCriticalIndex = index
			}

			if lastCriticalIndex != -1 {
				// so I don't need to check there are at least 2 nodes in else block
				minDistance = min(minDistance, distSinceLast)
			}

			// Since consecutive nodes are 1 node apart
			distSinceLast = 1

		} else {
			distSinceLast++
		}

		index++
		prevVal = curr.Val
		curr = curr.Next
	}

	if lastCriticalIndex == -1 {
		return []int{-1, -1}
	}
	return []int{minDistance, lastCriticalIndex - firstCriticalIndex}

}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// @leet end
