# https://leetcode.com/problems/koko-eating-bananas/solutions/769702/python-clear-explanation-powerful-ultimate-binary-search-template-solved-many-problems/


def binary_search(array: list) -> int:
    def condition(mid) -> bool:
        key = 5
        return key <= array[mid]

    # ensure left and right includes all elements
    left, right = 0, len(array)

    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1

    # left == min k that satisfies, left - 1 is last k that does not satisfy condition
    return left
