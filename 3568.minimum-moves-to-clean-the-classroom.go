package leetcode

// @leet start
type Vis struct {
	i          int
	j          int
	currEnergy int
}

type Pair struct {
	i int
	j int
}

func minMoves(classroom []string, energy int) int {
	n := len(classroom)
	m := len(classroom[0])

	visited := make(map[Pair]int)
	var starting Vis

	matrix := make([][]byte, n)
	for i := range n {
		matrix[i] = make([]byte, m)
		for j := range m {
			matrix[i][j] = classroom[i][j]
			if classroom[i][j] == 'S' {
				starting = Vis{i, j, energy}
			}
		}
	}

	dirs := []Pair{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}

	var stack []Vis
	stack = append(stack, starting)
	for len(stack) > 0 {
		curr := stack[0]
		stack = stack[1:]

		for _, dir := range dirs {
			ni, nj := curr.i+dir.i, curr.j+dir.j

		}

	}

}

// @leet end

