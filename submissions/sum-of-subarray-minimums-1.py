// https://leetcode.com/problems/sum-of-subarray-minimums

class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        n = len(arr)
        MOD = 10**9 + 7

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

        ple, nle = prev_less_elem(arr)

        sum = 0
        for i, ele in enumerate(arr):
            left = i - ple[i] if ple[i] != -1 else i + 1
            right = nle[i] - i if nle[i] != -1 else n - i
            sum += ele * left * right
            sum %= MOD

        return sum
