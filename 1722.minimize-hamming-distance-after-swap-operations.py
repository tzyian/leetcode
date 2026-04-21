# @leet imports start
from collections import Counter, defaultdict
from typing import List, Optional

# @leet imports end


# @leet start


class Solution:
    class UnionFind:
        def __init__(self) -> None:
            self.uf = dict()

        def union(self, a: int, b: int) -> None:
            rootA = self.find(a)
            rootB = self.find(b)
            self.uf[rootA] = rootB

        def find(self, a: int):
            if a not in self.uf:
                self.uf[a] = a
            if self.uf[a] != a:
                self.uf[a] = self.find(self.uf[a])
            return self.uf[a]

    def minimumHammingDistance(
        self, source: List[int], target: List[int], allowedSwaps: List[List[int]]
    ) -> int:
        n = len(source)
        # errors = [i for i in range(n) if source[i] != target[i]]

        uf = self.UnionFind()

        # group_counter[copmonent][target_num] = count of target_num
        group_counter = defaultdict(Counter)

        # make a undirected graph with all swaps
        for i, j in allowedSwaps:
            # NOTE: cannot skip, e.g.
            # src: [1,2,3,4]
            # tgt: [4,2,3,1]
            # swp:  * ^ ^ *
            # 2 and 3 serve as a bridge for 1 and 4
            # if source[i] == target[i] or source[j] == target[j]:
            #     continue
            uf.union(i, j)

        for i in range(n):
            f = uf.find(i)
            group_counter[f][source[i]] += 1

        ## NOTE: components with only 1 element but not within the swaps need to be aconted for in the next step
        # seen_idxes = set()
        # for i, j in allowedSwaps:
        #     if i not in seen_idxes:
        #         seen_idxes.add(i)
        #         f = uf.find(i)
        #         group_counter[f][source[i]] += 1
        #
        #     if j not in seen_idxes:
        #         seen_idxes.add(j)
        #         f = uf.find(j)
        #         group_counter[f][source[j]] += 1

        ans = 0

        # Find the common elements of source and target within the same component

        ## NOTE: must iterate across all elements rather than only errors
        # if iterating across errors, it doesnt account for swapping
        # for i in errors:

        for i in range(n):
            grp = uf.find(i)
            c = group_counter[grp]
            if c[target[i]] > 0:
                c[target[i]] -= 1
            else:
                ans += 1
        return ans

        # NOTE: doesn't account that swapping may introduce errors elsewhere
        # for each idx within errors,
        # remove this value from the group, and add this value
        # if the index is not an error
        # e.g. [3, 2]. we remove 2, and add 3. then at idx[1], we remove 3 and add 2
        # then we count the number of values left inside errors
        # for i in errors:
        #     grp = uf.find(i)
        #     c = group_counter[grp]
        #     if c[target[i]] > 0:
        #         c[target[i]] -= 1
        #         c[source[i]] += 1
        #         ans -= 1


# @leet end

s = [2, 3, 1]
t = [1, 2, 2]
sw = [[0, 2], [1, 2]]
x = Solution().minimumHammingDistance(s, t, sw)
print(x)
