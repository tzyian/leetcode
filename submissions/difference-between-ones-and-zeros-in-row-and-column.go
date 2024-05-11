// https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column

func onesMinusZeros(grid [][]int) [][]int {
    nRows := len(grid)
    nCols := len(grid[0])
    onesRow := make([]int, nRows)
    onesCol := make([]int, nCols)
    zeroesRow := make([]int, nRows)
    zeroesCol := make([]int, nCols)

    for i, row := range grid {
        for j, ele := range row {
            if ele == 1 {
                onesRow[i]++
                onesCol[j]++
            } else if ele == 0 {
                zeroesRow[i]++
                zeroesCol[j]++
            }
        }
    }

    diff := make([][]int, nRows)
    for i := range diff {
        diff[i] = make([]int, nCols)
    }

    for i, row := range grid {
        for j := range row {
            diff[i][j] = onesRow[i] + onesCol[j] - zeroesRow[i] - zeroesCol[j]
        }
    }

    return diff

}
