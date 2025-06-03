# @leet start
class ProductOfNumbers:

    def __init__(self):
        self.prefix_product = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_product = [1]
            return
        newvar = self.prefix_product[-1] * num
        self.prefix_product.append(newvar)

    def getProduct(self, k: int) -> int:
        if len(self.prefix_product) < k + 1:
            return 0
        ans = self.prefix_product[-1] // self.prefix_product[-k - 1]
        return ans


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
# @leet end

