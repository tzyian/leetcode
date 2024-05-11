// https://leetcode.com/problems/special-positions-in-a-binary-matrix

func numSpecial(mat [][]int) int {
    nRows := len(mat)
    nCols := len(mat[0])
    onesInRow := make([]int, nRows)
    onesInCol := make([]int, nCols)

    for i, row := range mat {
        for j, ele := range row {
            if ele == 1 {
                onesInRow[i]++
                onesInCol[j]++
            }
        }
    }


    numSpecial := 0
    for i, aEle := range onesInRow {
        for j, bEle := range onesInCol {
            if mat[i][j] == 1 && aEle == 1  && bEle == 1 {
                numSpecial++
            }
        }
    }

    return numSpecial

}
