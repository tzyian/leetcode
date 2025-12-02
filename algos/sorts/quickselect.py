def quickselect(arr: list[int], k: int) -> int:
    """
    Quickselect algorithm to find the k-th smallest element in an unsorted list.
    :param arr: List of integers
    :param k: Index (0-based) of the desired smallest element
    :return: The k-th smallest element in the list
    """
    if k < 0 or k >= len(arr):
        raise IndexError("k is out of bounds")

    def partition(lo: int, hi: int, pivot_index: int) -> int:
        pivot_value = arr[pivot_index]
        # Move pivot to end
        arr[pivot_index], arr[hi] = arr[hi], arr[pivot_index]
        store_index = lo
        for i in range(lo, hi):
            if arr[i] < pivot_value:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1
        # Move pivot to its final place
        arr[store_index], arr[hi] = arr[hi], arr[store_index]
        return store_index

    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        pivot_index = (lo + hi) // 2
        pivot_new_index = partition(lo, hi, pivot_index)
        if pivot_new_index == k:
            return arr[pivot_new_index]
        elif pivot_new_index < k:
            lo = pivot_new_index + 1
        else:
            hi = pivot_new_index - 1

    raise RuntimeError("Unexpected error in quickselect")
