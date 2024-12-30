# @leet start
from collections import deque
from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque()
        ans = 0

        queue.append(root)

        while queue:
            ls = []
            newqueue = deque()
            while queue:
                node = queue.popleft()
                ls.append(node.val)

                if node.left:
                    newqueue.append(node.left)
                if node.right:
                    newqueue.append(node.right)

            queue = newqueue
            ans += self.swaps(ls)

        return ans

    def swaps(self, ls: list[int]) -> int:
        def swap(ls: list, a: int, b: int) -> None:
            ls[a], ls[b] = ls[b], ls[a]

        curr_etoi = dict()
        lss = sorted(ls)
        swaps = 0


        for i, ele in enumerate(ls):
            curr_etoi[ele] = i

        for i, ele in enumerate(ls):
            expected_ele = lss[i]
            if ele != expected_ele:
                pos_expected = curr_etoi[expected_ele]
                swaps += 1
                swap(ls, pos_expected, i)

                curr_etoi[ls[pos_expected]] = pos_expected
                curr_etoi[ls[i]] = i

        return swaps


# @leet end

ls = [7, 6, 5, 4]
x = Solution().swaps(ls)
print(x)

