// https://leetcode.com/problems/k-radius-subarray-averages

# greedy heap to determine k radius average

from collections import deque

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        num_in_r = 2 * k + 1

        # no elements have enough radius
        if n < num_in_r:
            return [-1 for _ in range(n)]

        
        ans = [None for _ in range(n)]
        q = deque()
        qsum = 0

        # first k elements and last k elements are -1 because they do not have radius

        for i in range(n):

            # 0 to k-1 elements have no radius on left
            # n-k to n-1 elements have no radius on right
            if i < k or i >= n - k:
                ans[i] = -1 

            q.append(nums[i])
            qsum += nums[i]

            # pop if more than num_in_r so you can find the ave
            if len(q) > num_in_r:
                qsum -= q.popleft()

            # each time you find the ave, there are k on each side, then the middle
            # so the q has 2k+1 elements
            if len(q) == num_in_r:
                ans[i - k] = qsum // num_in_r

        
        return ans

      