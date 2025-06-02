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
        swap(arr, i, j)
