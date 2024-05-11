// https://leetcode.com/problems/total-cost-to-hire-k-workers

import random

def partition(nums, low, high):
    pass

def quickselect(nums, k):
    pass



from heapq import heappush, heappop, heapify, nsmallest
class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        n = len(costs) # this is the number of available workers
        
        # edge case where all workers are hired which the constraint takes care of
        if n <= k:
            return sum(costs)

        # case where all workers come from the same pq
        elif n <= 2 * candidates:
            # return smallest n values using qselect or heap
            costs.sort() # should use quickselect here
            # quickselect(costs, k)
            return sum(costs[0:k])
        

        # else use the heapleft and heapright approach

        totalcost = 0

        x = candidates # look at the first x and last x workers

        leftheap = costs[0:x]       # worker list counting from left
        heapify(leftheap)
        rightheap = costs[-x:n]     #         ''           from right
        heapify(rightheap)

        leftindex = x               # the first index counting from left not part of the heap
        rightindex = n - x - 1      #       ''                 from right       ''
        
        num_to_be_hired = k
        while num_to_be_hired > 0:
            if leftindex <= rightindex: 
                # the case where it starts leftindex < rightindex is handled before the while
                # once leftindex > rightindex, then there are less than 2x workers remaining
                if leftheap[0] <= rightheap[0]: # take from left heap
                    totalcost += heappop(leftheap)
                    heappush(leftheap, costs[leftindex])
                    leftindex += 1
                else:
                    totalcost += heappop(rightheap) # take from right heap
                    heappush(rightheap, costs[rightindex])
                    rightindex -= 1
            # if not, there are less than 2x workers remaining and either heap can become empty
            elif leftheap and rightheap:
                if leftheap[0] <= rightheap[0]: # take from left heap
                    totalcost += heappop(leftheap)
                else: #take from rightheap
                    totalcost += heappop(rightheap)
            elif leftheap:
                totalcost += heappop(leftheap)
            else:
                totalcost += heappop(rightheap)
            print(totalcost)
            


            num_to_be_hired -= 1
        return totalcost

