// https://leetcode.com/problems/top-k-frequent-elements

import random

def partition2way(ls, start, stop):
    pIndex = random.randint(start, stop)
    n = stop - start + 1
    pivot = ls[pIndex]
    swap(ls, start, pIndex)
    low = start + 1
    high = stop + 1
    while low < high:
        while low < high and ls[low][1] >= pivot[1]:
            low += 1
        while low < high and (high > stop or ls[high][1] < pivot[1]):
            high -= 1
        if (low < high):
            swap(ls, low, high)
    swap(ls, start, low - 1)
    return low - 1
    
def swap(ls, i, j):
    ls[i], ls[j] = ls[j], ls[i]


#3 way partition
def partition(arr, low, high):
    pIndex = random.randint(low, high)
    pivot = arr[pIndex]
    i = low
    mid = low
    j = high
    print(pivot)

    while mid <= j:
        if arr[mid][1] > pivot[1]:
            arr[mid], arr[i] = arr[i], arr[mid]
            i += 1
            mid += 1
        elif arr[mid][1] == pivot[1]:
            mid += 1
        else:
            arr[mid], arr[j] = arr[j], arr[mid]
            j -= 1

    # i and j are start and end indices equal to pivot
    return i, j




class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = Counter(nums)
        ls = list(table.items())
        n = len(ls)
        
        return self.helper(ls, k, 0, n - 1)
        
        
    def helper(self, ls, k, start, stop):
        a, b = partition(ls, start, stop)
        if k - 1 in range(a, b+1):
            return [key for key, value in ls[:k]]
        elif a < k - 1:
            return self.helper(ls, k, b + 1, stop)
        else:
            return self.helper(ls, k, start, a - 1)
        
