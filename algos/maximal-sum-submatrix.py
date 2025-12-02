def maximal_sum_submatrix(matrix: list[list[int]]) -> int:
    # Time complexity: O(cols^2 * rows)
    # Space complexity: O(rows)

    # You run through all pairs of columns (O(cols^2)),
    # and for each pair, you compute the row sums and run Kadane's algorithm (O(rows)).

    if not matrix or not matrix[0]:
        return 0

    inf = 10**9

    max_sum = -inf
    rows, cols = len(matrix), len(matrix[0])

    # fix the columns, run Kadane (maximum subarray sum) on row sums
    for left in range(cols):
        row_sums = [0] * rows
        for right in range(left, cols):
            for row in range(rows):
                row_sums[row] += matrix[row][right]

            current_sum = 0
            current_max = -inf
            for value in row_sums:
                current_sum += value
                current_max = max(current_max, current_sum)
                if current_sum < 0:
                    current_sum = 0

            max_sum = max(max_sum, current_max)

    return max_sum


# Example usage:
matrix = [
    [0, -2, -7, 0],
    [9, 2, -6, 2],
    [-4, 1, -4, 1],
    [-1, 8, 0, -2],
]
result = maximal_sum_submatrix(matrix)
print(result)  # 15
