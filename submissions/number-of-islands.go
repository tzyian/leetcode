// https://leetcode.com/problems/number-of-islands

func numIslands(grid [][]byte) int {
	count := 0
	for r, row := range grid {
		for c, ele := range row {
			if ele == '1' {
				count++
				bfs(c, r, grid)

			}
		}
	}

	return count
}

type Coord struct {
	x int
	y int
}

// bfs mutates the grid
func bfs(i, j int, grid [][]byte) {
	var queue []*Coord
	visited := make(map[*Coord]struct{})
	queue = append(queue, &Coord{i, j})

	for len(queue) > 0 {
		var curr *Coord
		curr, queue = queue[0], queue[1:]

		if curr.y < 0 || curr.y >= len(grid) || curr.x < 0 || curr.x >= len(grid[0]) {
			continue
		}

		if _, ok := visited[curr]; !ok {
			visited[curr] = struct{}{}

			if grid[curr.y][curr.x] == '1' {
				grid[curr.y][curr.x] = '0'
				queue = append(queue, &Coord{curr.x, curr.y - 1}) // up
				queue = append(queue, &Coord{curr.x, curr.y + 1}) // down
				queue = append(queue, &Coord{curr.x - 1, curr.y}) // left
				queue = append(queue, &Coord{curr.x + 1, curr.y}) // right
			}
		}

	}

}
