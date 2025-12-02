class StockSpanner:
    def __init__(self):
        # a span is
        # [34, 7, 2, 1, 2] + [2]
        #      ^              $
        # has span of 4
        self.n = 0
        self.stack = []

    # mono increasing
    def next(self, price: int) -> int:
        # top element is the smallest index <= curr
        self.n += 1
        stack = self.stack
        while stack and stack[-1][1] <= price:
            stack.pop()

        if stack:
            ans = self.n - stack[-1][0]
        else:
            ans = self.n

        stack.append((self.n, price))
        return ans


# 3542. Minimum Operations to Convert All Elements to Zero
# , set all instances of minimum value to 0
# Then find the number of such segments
class MinimumOperations:
    def minOperations(self, nums: list[int]) -> int:
        # find the largest contiguous non-zero subarray and zero it
        ans = 0

        stack = []  # mono increasing
        for x in nums:
            while stack and stack[-1] > x:
                stack.pop()

            if x == 0:
                continue

            if not stack or x != stack[-1]:
                stack.append(x)
                ans += 1

        return ans
