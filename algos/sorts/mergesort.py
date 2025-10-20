def merge_sort(arr: list[int]) -> tuple[list[int], int]:
    n = len(arr)
    if n <= 1:
        return arr, 0

    mid = n // 2
    a, ainvs = merge_sort(arr[:mid])
    b, binvs = merge_sort(arr[mid:])
    c, cinvs = merge(a, b)
    # out of orders from [0,mid), [mid, n), and cross inversions
    return c, ainvs + binvs + cinvs


def merge(a: list[int], b: list[int]) -> tuple[list[int], int]:
    arr = []
    invs = 0
    i, j = 0, 0
    n, m = len(a), len(b)
    while i < n and j < m:
        if a[i] <= b[j]:
            arr.append(a[i])
            i += 1
        else:
            arr.append(b[j])
            invs += n - i  # NOTE: this is the line that is added
            j += 1
    for k in range(i, n):
        arr.append(a[k])
    for k in range(j, m):
        arr.append(b[k])
    return arr, invs


arr = [6, 5, 3, 1, 23, 24, 25, 29, 30, 1]
x, invs = merge_sort(arr)
print(x)
print(invs)
