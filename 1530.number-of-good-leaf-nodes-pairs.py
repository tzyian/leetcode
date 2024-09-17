# @leet start
# Definition for a binary tree node.
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> defaultdict[int]:
        pairs = 0

        def dfs(node: TreeNode) -> int:
            nonlocal pairs

            if not node:
                return defaultdict(int)
            elif not node.left and not node.right:
                count = defaultdict(int)
                count[1] = 1
                return count

            left_dist = dfs(node.left)
            right_dist = dfs(node.right)

            for d1 in left_dist:
                if d1 > distance:
                    continue
                for d2 in right_dist:
                    if d1 + d2 <= distance:
                        pairs += left_dist[d1] * right_dist[d2]

            all_dist = defaultdict(int)
            for d in left_dist:
                if d + 1 <= distance:
                    all_dist[d + 1] += left_dist[d]
            for d in right_dist:
                if d + 1 <= distance:
                    all_dist[d + 1] += right_dist[d]
            return all_dist

        dfs(root)
        return pairs

    def countPairsArray(self, root: TreeNode, distance: int) -> int:
        pairs = 0

        def dfs(node: TreeNode) -> int:
            nonlocal pairs

            if not node:
                return []
            elif not node.left and not node.right:
                return [1]

            left_dist = dfs(node.left)
            right_dist = dfs(node.right)

            for d1 in left_dist:
                if d1 > distance:
                    continue
                for d2 in right_dist:
                    if d1 + d2 <= distance:
                        pairs += 1

            all_dist = left_dist + right_dist
            return [d + 1 for d in all_dist]

        dfs(root)
        return pairs


# @leet end
