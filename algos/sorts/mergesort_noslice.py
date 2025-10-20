from typing import List


# only 1 array copy per merge instead of 2


def count_inversions(arr: List[int]) -> int:
    n = len(arr)
    temp = [0] * n

    # [lo:hi)
    def merge_sort(lo: int, hi: int) -> int:
        if hi - lo <= 1:
            return 0
        mid = (lo + hi) // 2

        invs = 0
        invs += merge_sort(lo, mid)
        invs += merge_sort(mid, hi)

        # merge
        i, j, k = lo, mid, lo
        while i < mid and j < hi:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                j += 1
                invs += mid - i  # all remaining in left are > arr[j]
            k += 1
        while i < mid:
            temp[k] = arr[i]
            i += 1
            k += 1
        while j < hi:
            temp[k] = arr[j]
            j += 1
            k += 1

        arr[lo:hi] = temp[lo:hi]
        return invs

    return merge_sort(0, n)
