def quicksort(arr: list[int], lo: int, hi: int) -> list[int]:
    if lo < hi:
        p = partition(arr, lo, hi)
        quicksort(arr, lo, p - 1)
        quicksort(arr, p + 1, hi)
    return arr


def swap(arr: list[int], i: int, j: int):
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr: list[int], lo: int, hi: int):
    pivot = arr[hi]
    i = lo - 1
    j = hi + 1
    # Hoare partition
    while True:
        while True:
            i += 1
            if arr[i] >= pivot:
                break
        while True:
            j -= 1
            if arr[j] <= pivot:
                break
        if i >= j:
            return j
        # we want i, j to be the last swapped position
        # hence lo and hi starts outside the array bounds
        swap(arr, i, j)


def lomuto_partition(arr: list[int], lo: int, hi: int):
    pivot = arr[hi]
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i + 1, hi)
    return i + 1
