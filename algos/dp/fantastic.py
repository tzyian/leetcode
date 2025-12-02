"""
CS3230 Tut

Given
arr is tuples of [ai, bi], where 0 <= ai, bi

Find the minimum size of a subset of arr, S, where
    sum ai in S >= A/2
    sum bi in S >= B/2
"""

from math import ceil


def fantastic_papers(arr: list[tuple[int, int]]) -> int:
    A = sum(x[0] for x in arr)
    B = sum(x[1] for x in arr)
    ah = ceil(A / 2)
    bh = ceil(B / 2)

    inf = 10**10
    dp = [[inf] * (bh + 1) for _ in range(ah + 1)]

    dp[0][0] = 0

    # unbounded
    # note iterate items first, and forwards or backwards is fine
    for i in range(ah + 1):
        for j in range(bh + 1):
            for a, b in arr:
                dp[i][j] = min(1 + dp[max(i - a, 0)][max(j - b, 0)], dp[i][j])

    # only once
    # note iterate coins first, then backwards
    # backwards so the state of ah_i is only counted once for every a, b
    # note if you iterate forwards, dp[i][j] may already have been updated
    for a, b in arr:
        for i in range(ah, -1, -1):
            for j in range(bh, -1, -1):
                dp[i][j] = min(1 + dp[max(i - a, 0)][max(j - b, 0)], dp[i][j])

    return dp[ah][bh]


# Small basic
# print(fantastic_papers([(1, 1)]))

# # Multiple same items
# print(fantastic_papers([(2, 2), (2, 2), (2, 2)]))
#
# # Mixed values
# print(fantastic_papers([(3, 1), (1, 3), (2, 2)]))
#
# # Edge case: uneven sums
# print(fantastic_papers([(5, 1), (1, 7), (2, 2)]))
print(
    fantastic_papers(
        [(100, 1), (1, 1), (1, 20), (1, 20), (1, 20), (1, 1), (1, 1), (1, 1), (1, 1)]
    )
)
#
# # Larger values
# print(fantastic_papers([(10, 5), (3, 12), (7, 4), (6, 8)]))
#
# # Many small pairs
# print(fantastic_papers([(1, 2), (2, 1), (1, 1), (2, 2), (1, 3), (3, 1)]))
#
# # One large dominating pair
# print(fantastic_papers([(100, 1), (1, 100)]))
#
# # Balanced but sparse
# print(fantastic_papers([(10, 10), (5, 5), (20, 0), (0, 20)]))
