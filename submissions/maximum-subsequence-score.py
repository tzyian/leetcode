// https://leetcode.com/problems/maximum-subsequence-score

class Solution:
    '''
    recall a subsequence keeps order but not contiguity
    1 2 3 4 5 can pick 1 3 5

    Algo:
    Since algo only wants max score, what the indices are don't matter.
    
    Zip nums1 and nums2 and sort by nums2.    
    Once num2 is sorted (descending), the kth element is always the kth largest, you can pick the k indices smaller than it.
    Since num1 and num2 are already paired and sorted, you just need to check the k elements before.
    To find the largest sum of elements of num1 in pairs[0..k-1], keep a min heap and find the sum  of the elements in the heap. To do this, keep a counter that sums the push as you push, and deducts the pop as you pop.
    Then you can find the max score of a particular subsequence with num2 > pairs[k-1].
    
    To find the largest score out of all subsequences, you need to iterate across the pairs. BUT you already have the max sum out of the heap from pairs[0..k-1]. So overlapping substructure. Then just need to pop the smallest element from the heap and add the new element of pairs[k]. You don't need to care about min(num2) in pairs[k] since it's just the next element in pairs[].

    After pop and add the next element, you can then find your score of k elements from the pairs[0..k] (which is k+1 elements)

    Then just iterate.


    '''
    from heapq import heappush, heappop, heapify

    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(a,b) for a,b in zip(nums1, nums2)]
        pairs.sort(key = lambda x: -x[1])
        heap = []
        heapify(heap)
        heapsum = 0
        maxscore = 0
        
        
        for i in range(k):
            # the min of num2 pairs[k-1][1] which is desc_sorted_num2[k-1]
            heappush(heap, pairs[i][0])
            heapsum += pairs[i][0]
            #heapsum is then the sum of num1 of these k elements
        maxscore = heapsum * pairs[i][1]
        
        for i in range(k, len(pairs)):
            heappush(heap, pairs[i][0])
            heapsum += pairs[i][0]
            heapsum -= heappop(heap)
            maxscore = max(maxscore, heapsum * pairs[i][1])

        return maxscore










