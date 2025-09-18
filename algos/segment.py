from typing import List

# https://leetcode.com/problems/range-sum-query-mutable/solutions/75784/python-well-commented-solution-using-segment-trees/comments/221486/
#  which is adapted from
# https://codeforces.com/blog/entry/18051


# @leet start
class NumArray:

    def __init__(self, nums: List[int]):
        l = len(nums)
        # a bin heap structure with the original array as leaf nodes
        tree = [0] * l + nums
        for i in range(l - 1, 0, -1):
            # parent is sum of of nodes
            tree[i] = tree[i * 2] + tree[i * 2 + 1]

        self.l = l
        self.tree = tree

    def update(self, index: int, val: int) -> None:
        tree = self.tree

        # change n to the leaf node
        i = self.l + index

        # update the leaf node
        tree[i] = val

        while i > 1:
            # i is now the parent
            i >>= 1
            tree[i] = tree[i * 2] + tree[i * 2 + 1]
            # you can micro-optimise by terminating if tree[i] didn't change
            # if tree[i] == new_value:
            #     break
            # else:
            #     tree[i] = new_value

            ### alternate style: parent node is the sum of the 2 child nodes
            ### If n is even (...0), then n ^ 1 = n + 1 (its right sibling).
            ### If n is odd (...1), then n ^ 1 = n - 1 (its left sibling).
            # while i > 1:
            #      tree[i >> 1] = tree[i] + tree[i ^ 1]
            #      i >>= 1

    def sumRange(self, left: int, right: int) -> int:
        # [left, right)

        # change left and right to the leaf nodes
        lo = self.l + left
        hi = self.l + right + 1  # note: add 1 here to simulate exclusive range

        res = 0

        while lo < hi:
            # odd means right child. Interval includes lo but not parent
            if lo & 1:
                res += self.tree[lo]
                lo += 1

            # odd means right child (not included)
            # hi -= 1 to find the left child (included)
            if hi & 1:
                hi -= 1
                res += self.tree[hi]

            lo >>= 1
            hi >>= 1
        return res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
# @leet end
