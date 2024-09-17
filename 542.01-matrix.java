// @leet start
class Solution {
    public int[][] updateMatrix(int[][] mat) {
        // TC: O(m*n)
        // SC: O(1)
        int nrows = mat.length;
        int ncols = mat[0].length;
        int inf = 1_000_000_000;

        for (int i = 0; i < nrows; i++) {
            for (int j = 0; j < ncols; j++) {
                if (mat[i][j] == 0) {
                    continue;
                }
                int top = inf;
                int left = inf;
                if (i - 1 >= 0) {
                    top = mat[i - 1][j];
                }
                if (j - 1 >= 0) {
                    left = mat[i][j-1];
                }
                mat[i][j] = 1 + Math.min(top, left);
            }
        }

        for (int i = nrows - 1; i >= 0; i--) {
            for (int j = ncols - 1; j >= 0; j--) {
                if (mat[i][j] == 0) {
                    continue;
                }
                int bottom = inf;
                int right = inf;
                if (i + 1 < nrows) {
                    bottom = mat[i + 1][j];
                }
                if (j + 1 < ncols) {
                    right = mat[i][j + 1];
                }
                // Two mins because mat[i][j] could be lower from the above loop
                mat[i][j] = Math.min(mat[i][j], 1 + Math.min(bottom, right));
            }
        }

        return mat;

    }
}
// @leet end
