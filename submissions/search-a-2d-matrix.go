// https://leetcode.com/problems/search-a-2d-matrix

// (since i previously did search 2d as 1d matrix, do double binary search here)
// binary search the first index, then see whether to search up or search down. 
// Row to search is where matrix[n][0] <= target < matrix[n + 1][0] 
// Once find the row to search, binary search that row to find whether inside

func searchMatrix(matrix [][]int, target int) bool {
    // SC: constant, TC: log(m)*log(n)
    nRows := len(matrix)

    lo := 0
    hi := nRows - 1

    for lo < hi {
        mid := lo + (hi - lo + 1) / 2
        if matrix[mid][0] > target {
            // search up
            hi = mid - 1
        } else {
            // search down
            lo = mid
        }
    }

    return binarySearchRow(matrix[lo], target)

}

func binarySearchRow(row []int, target int) bool {
    // SC: constant. TC: logm
    n := len(row)
    lo := 0
    hi := n - 1
    for lo <= hi {
        mid := lo + (hi - lo) / 2
        if row[mid] == target {
            return true
        } else if row[mid] < target {
            // search right
            lo = mid + 1
        } else {
            // search left
            hi = mid - 1
        }
    }
    
    return false
}