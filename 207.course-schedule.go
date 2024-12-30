package leetcode

// @leet start
func canFinish(numCourses int, prerequisites [][]int) bool {
	// Kahn's algo for topo sort

	// Generate adjacency list
	adjList := make([][]int, numCourses)
	for i := range numCourses {
		adjList[i] = make([]int, 0)
	}

	// For calculating indegrees
	reverseAdj := make([][]int, numCourses)

	for _, prereq := range prerequisites {
		pre := prereq[1]
		post := prereq[0]

		adjList[pre] = append(adjList[pre], post)

		reverseAdj[post] = append(reverseAdj[post], pre)
	}

	// Compute indegrees
	zeros := make([]int, 0)
	indegrees := make([]int, numCourses)

	for i, fromNodes := range reverseAdj {
		indegrees[i] = len(fromNodes)
		if indegrees[i] == 0 {
			zeros = append(zeros, i)
		}
	}

	count := 0
	for len(zeros) > 0 {
		curr := zeros[0]
		zeros = zeros[1:]
		count++

		for _, node := range adjList[curr] {
			indegrees[node]--
			if indegrees[node] == 0 {
				zeros = append(zeros, node)
			}
		}
	}

	return count == numCourses
}

// @leet end

