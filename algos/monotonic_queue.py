# 1696 Jump Game VI is DP +
# 239 Sliding Window Maximum
# In O(n) time


from collections import deque

# From 0 to n-1
# At each index i, you can jump at most k steps forward
# Return the maximum score you can get to reach the last index


def maxResult(nums: list[int], k: int) -> int:
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    deq = deque([0])

    # we want a monotonic deque
    # old elements are at the left
    # new elements are at the right
    # and the deque is monotonically decreasing
    for i in range(1, n):
        while deq and deq[0] < i - k:
            deq.popleft()

        best = dp[deq[0]]
        dp[i] = nums[i] + best

        while deq and dp[deq[-1]] <= dp[i]:
            deq.pop()
        deq.append(i)

    return dp[n - 1]


# @leet end

x = ""
n = [1, -1, -2, 4, -7, 3]
k = 2
x = maxResult(n, k)
print(x)  # 7

n = [10, -5, -2, 4, 0, 3]
k = 3
x = maxResult(n, k)
print(x)  # 17

n = [1, -5, -20, 4, -1, 3, -6, -3]
k = 2
x = maxResult(n, k)
print(x)  # -
