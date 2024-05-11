// https://leetcode.com/problems/sum-of-subarray-minimums

# adapted from https://leetcode.com/problems/sum-of-subarray-minimums/solutions/178876/stack-solution-with-very-detailed-explanation-step-by-step/?envType=daily-question&envId=2024-01-20
# there are other solutions eg https://leetcode.com/problems/sum-of-subarray-minimums/solutions/257811/python-o-n-slightly-easier-to-grasp-solution-explained/?envType=daily-question&envId=2024-01-20

class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        n = len(arr)
        MOD = 10**9 + 7

        # monotonic non-decreasing stack with both lte and gt at index
        def prev_less_elem(arr: list[int]) -> tuple[list[int], list[int]]:
            ple = [-1] * n
            nle = [-1] * n
            stack = []
            for i, ele in enumerate(arr):
                while stack and arr[stack[-1]] > ele:
                    next_ele = stack.pop()
                    nle[next_ele] = i
                ple[i] = stack[-1] if stack else -1
                stack.append(i)
            return ple, nle
        # here, ple is lte, while nle is gt. eg: 111 from 0th index and 111 from 2nd index are both 111, to only account for dupes sequences once 
        # if you want ple to be lt, use `arr[stack[-1]] >= ele` because then it'll be out of the loop (just trace the code).
        # nle is gt because it's within the loop (just trace)

        ple, nle = prev_less_elem(arr)

        sum = 0
        for i, ele in enumerate(arr):
            # if left is -1, then no elements lte on the left. there are i+1 subarrays ending in arr[i]
            # if right is -1, then no elements lt on the right, there are n-1-(i+1) subarrays on the right
            left = i - ple[i] if ple[i] != -1 else i + 1
            right = nle[i] - i if nle[i] != -1 else n - i
            # mod arithmetic here
            sum += ele * left * right
            sum %= MOD

        return sum
