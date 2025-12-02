# @leet imports start

# @leet imports end


# @leet start
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


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @leet end
