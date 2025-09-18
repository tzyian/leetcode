# https://leetcode.com/problems/koko-eating-bananas/solutions/769702/python-clear-explanation-powerful-ultimate-binary-search-template-solved-many-problems/

"""
binary search variants
1. First valid
2. Last valid
3. Range
4. Local max
5. Local min
6.
"""

from typing import Callable

# last_valid: exclusive hi: lo = mid + 1, return lo -1
# first_valid: exclusive hi: lo = mid + 1, return lo


def last_valid(arr: list, valid: Callable) -> int:
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if valid(mid):
            lo = mid + 1
        else:
            hi = mid
    return lo - 1


def first_valid(array: list, valid: Callable) -> int:
    lo, hi = 0, len(array)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if valid(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


# allowing a[n-1] to be valid, hence need to check i+1 < len(a)
def first_valid_bitonic(a):
    valid = lambda i: a[i] >= (a[i + 1] if i + 1 < len(a) else float("-inf"))
    return first_valid(a, valid)


# allowing a[0] to be valid, hence need to check i-1 >= 0
def last_valid_bitonic(a):
    valid = lambda i: (a[i - 1] if i - 1 >= 0 else float("-inf")) <= a[i]
    return last_valid(a, valid)


def find_range(arr: list, valid: Callable, valid2: Callable) -> tuple:
    """
    Find the range [first, last] where valid is True.
    E.g. to find the range of values within a target range, use
    valid = lambda x: arr[x] >= target_low
    valid2 = lambda x: arr[x] <= target_high
    """
    first = first_valid(arr, valid)
    last = last_valid(arr, valid2)
    return (first, last)


def binary_search_float(
    lo: float,
    hi: float,
    P: Callable[[float], bool],
    eps: float = 1e-9,
    max_iter: int = 200,
) -> float:
    """
    Min x in [lo, hi] such that P(x) is True (monotone False->True).
    Stops when interval <= eps or iterations exhausted. Returns midpoint.
    """
    for _ in range(max_iter):
        mid = (lo + hi) / 2.0
        if P(mid):
            hi = mid
        else:
            lo = mid
        if hi - lo <= eps:
            break
    return (lo + hi) / 2.0
