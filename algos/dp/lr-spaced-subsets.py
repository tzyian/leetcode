from bisect import bisect_left, bisect_right
from functools import cache

# Given a sorted array of non-negative distinct integers,
# must have gap of l between consecutive values
# total must sum up to r
# Count number of such subsequences

# TC: O(rn^2)
# Ideal TC: O(rnlogn) using segtree/fenwick or binary search???


def count_spaced_subsets(S: list[int], r: int, l: int) -> int:
    A = sorted(S)
    n = len(A)

    # dp[i][j] = no. of subsets from A[i..n-1] that sum to j
    dp = [[0 for _ in range(r + 1)] for _ in range(n + 1)]

    # dp[n][0] = 1 (empty subset)

    # dp[i][j] = dp[i+1][j] + (A[i] <= j ? dp[f(i)][j - A[i]] : 0)
    # where f(i) = smallest index > i such that A[f(i)] - A[i] >= l

    # dp[i+1][j] = subsets excluding A[i]
    # dp[f(i)][j - A[i]] = subsets including A[i]

    dp[n][0] = 1

    # precompute f_i, the smallest index > i such that A[f(i)] - A[i] >= l
    next_valid = [0] * n
    right = 0
    for left in range(n):
        while right < n and A[right] < A[left] + l:
            right += 1
        next_valid[left] = right

    for i in range(n - 1, -1, -1):
        f_i = next_valid[i]

        for j in range(r + 1):
            exclude_count = dp[i + 1][j]

            include_count = 0
            if A[i] <= j:
                include_count = dp[f_i][j - A[i]]

            dp[i][j] = exclude_count + include_count

    return dp[0][r]


def lr_spaced_subset(arr: list[int], l: int, r: int) -> int:
    ans = 0
    n = len(arr)

    # O(rn) possible combinations
    @cache
    def backtrack(start: int, tot: int) -> None:
        nonlocal ans
        if start >= n or tot > r:
            return
        if tot == r:
            ans += 1
            return

        next_index = bisect_left(arr, arr[start] + l, lo=start)
        for i in range(next_index, n):
            backtrack(i, tot + arr[i])

    # O(n) iteration
    for i in range(n):
        backtrack(i, arr[i])

    return ans


if __name__ == "__main__":
    S1 = [1, 2, 3, 4, 5, 7]
    target_r1 = 7
    spacing_l1 = 2
    # Possible subsets of {1,2,3,4,5} summing to 7 with dist >= 2:
    # {2, 5} (|2-5|=3 >= 2) -> Valid
    # {3, 4} (|3-4|=1 < 2)  -> Invalid
    # {7} -> Valid
    # {1, 6} (not in set)
    # {1, 2, 4} (|1-2|=1 < 2) -> Invalid
    # Let's test the code
    print(
        f"Count for S={S1}, r={target_r1}, l={spacing_l1}: {count_spaced_subsets(S1, target_r1, spacing_l1)}"
    )
