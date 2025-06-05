from typing import List


# @leet start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # ok a custom priority queue with hashmap for mutating node values + deletes
        # or dict/linkedlist + bsearch correct insertion point
        # will give nlogk time
        # the goal is to find one in linear time...????
        # i rmb there was some recursive trick to this...
        # ok the recursive stack is still k * n = n^2

        stack = []  # monotonic non-decreasing stack
        n = len(nums)
        ans = []

        def ins_stack(x: int, i: int) -> None:
            if not stack:
                stack.append((x, i))

            top = stack.pop()
            if x >= top[0]:
                stack.append((x, i))
            else:
                ins_stack(x, i)
                stack.append(top)

        for i in range(n):
            ins_stack(nums[i], i)

            if i >= k - 1:
                while True:
                    tx, ti = stack[-1]
                    if ti <= i - k:
                        stack.pop()
                    else:
                        ans.append(tx)
                        break

        return ans


# @leet end

ls = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
ls = [1, -1]
k = 1
x = Solution().maxSlidingWindow(ls, k)
print(x)

