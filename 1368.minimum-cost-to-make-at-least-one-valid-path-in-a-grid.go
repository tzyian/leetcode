package leetcode

import "math"

// @leet start
type coord struct {
	i, j int
}

func minCost(grid [][]int) int {
	n := len(grid)
	m := len(grid[0])
	dirs := map[int]coord{
		1: {0, 1},  // right
		2: {0, -1}, // left
		3: {1, 0},  // down
		4: {-1, 0}, // up
	}

	// 0-1 bfs
	root := coord{0, 0}

	dists := make([][]int, n)
	for i := range dists {
		dists[i] = make([]int, m)
		for j := range dists[i] {
			dists[i][j] = math.MaxInt
		}
	}
	dists[0][0] = 0

	queue := []coord{root}

	for len(queue) > 0 {
		curr := queue[0]
		queue = queue[1:]

		for dir := 1; dir <= 4; dir++ {
			i, j := curr.i, curr.j
			di, dj := dirs[dir].i, dirs[dir].j
			ni, nj := i+di, j+dj

			if 0 <= ni && ni < n && 0 <= nj && nj < m {
				cost := 0
				if dir != grid[i][j] {
					cost = 1
				}

				if dists[i][j]+cost < dists[ni][nj] {
					dists[ni][nj] = dists[i][j] + cost
					next := coord{ni, nj}
					if cost == 0 {
						queue = append([]coord{next}, queue...) // prepend
					} else {
						queue = append(queue, next) // append
					}
				}
			}
		}
	}

	return dists[n-1][m-1]

}

// @leet end

