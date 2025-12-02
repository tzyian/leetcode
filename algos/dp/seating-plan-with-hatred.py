"""
There are 2n guests, with n guests in a line on each side of the host.
The host (sitting in the middle) wants guests with higher favourability scores to sit closer to him.
Each guest has a mutual hatred with another guest (i.e. if A sits next to B and C, the hatred score increases by hatred[A][B] + hatred[A][C]).
No guest hates the host

favourability: List[int]
hatred: List[List[int]]

Find the minimum total hatred score based on the seating arrangement.

In O(n^3) time complexity.
"""


def min_hatred(favourability: list[int], hatred: list[list[int]]) -> int:
    pass
