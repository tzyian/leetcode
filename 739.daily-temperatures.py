from typing import List


# @leet start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # This is a monotonic decreasing stack problem
        stack = []
        n = len(temperatures)
        result = [0] * n
        for i in reversed(range(n)):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if not stack:
                result[i] = 0
            else:
                result[i] = stack[-1] - i
            stack.append(i)

        return result


# @leet end

t = [73, 74, 75, 71, 69, 72, 76, 73]
x = Solution().dailyTemperatures(t)
print(x)

t = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]
x = Solution().dailyTemperatures(t)
print(x)
e = [8, 1, 5, 4, 3, 2, 1, 1, 0, 0]
