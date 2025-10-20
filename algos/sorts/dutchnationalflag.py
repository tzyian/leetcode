# pivot == 1
def three_way_partition(arr, pivot):
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] < pivot:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == pivot:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr


# Example
print(three_way_partition([3, 5, 2, 5, 6, 1, 5, 7, 5], 5))
# -> [3,2,1,5,5,5,5,7,6] (order inside groups not guaranteed)
