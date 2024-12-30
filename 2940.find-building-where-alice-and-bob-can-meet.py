# @leet start
from heapq import heappop, heappush
from typing import List

QueryIdx = int
HeapKey = int
Heap = list[tuple[HeapKey, QueryIdx]]


class Solution:
    def leftmostBuildingQueries(
        self, heights: List[int], queries: List[List[int]]
    ) -> List[int]:
        sorted_heights = [(h, i) for i, h in enumerate(heights)]
        sorted_heights.sort()

        h = len(heights)
        q = len(queries)
        ans = [-1] * q
        # stack invariant: stack is sorted in descending order of heights
        stack: Heap = []
        query_store: list[Heap] = [[] for _ in range(h)]

        for i, (a, b) in enumerate(queries):
            if a > b:
                a, b = b, a

            if a == b or heights[a] < heights[b]:
                ans[i] = b
            else:
                # heights[a] is guaranteed to be >= heights[b]
                query_store[b].append((heights[a], i))

        for i in range(h - 1, -1, -1):
            s = len(stack)
            # for every query that needs building >= i
            # see if there are any buildings in the stack that are taller than heights[a]

            # you iterate this query_store q times across all iterations
            # each bsearch is a log(h) operation
            for ha, q_idx in query_store[i]:
                position = self.binary_search(stack, ha)
                if position < s and position >= 0:
                    ans[q_idx] = stack[position][1]

            # remove elements from top of stack (list back) that are <= than heights[i]
            # stack is there just for the bsearch
            while stack and stack[-1][0] <= heights[i]:
                stack.pop()
            # add current building to stack
            # so the top of the stack is always the shortest building,
            #  maintaining the invariant
            stack.append((heights[i], i))

        return ans

    def binary_search(self, stack, target):
        l, r = 0, len(stack) - 1
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if stack[mid][0] > target:
                ans = max(ans, mid)
                l = mid + 1
            else:
                r = mid - 1
        return ans

    # using PQ
    def leftmostBuildingQueries_pq(
        self, heights: List[int], queries: List[List[int]]
    ) -> List[int]:

        h = len(heights)
        q = len(queries)
        ans = [-1] * q

        heap: Heap = []
        # a query (a, b),
        # list of h lists of queries
        # mapped by q_idx, where q_idx = max(a,b)
        # i.e. each idx stores queries that can potentially answered by heights[i]
        query_store: list[Heap] = [[] for _ in range(h)]

        for i, (a, b) in enumerate(queries):
            # ensure indices a < b
            if a > b:
                a, b = b, a

            if a == b or heights[a] < heights[b]:
                ans[i] = b
            else:
                # heights[a] guaranteed to be >= heights[b]
                query_store[b].append((heights[a], i))

        for i, height in enumerate(heights):
            # this happens log(q) times across all loops
            while heap and (q_height := heap[0][0]) < height:
                # a heap is used because we want to find the smallest height
                # the queries are in a minheap with key=max(a, b)
                # so we can pop the smallest height that can be answered by the current building

                # if the current building height is smaller than the current query height,
                # then no query can be answered by this building, so just continue
                _, q_idx = heappop(heap)
                ans[q_idx] = i

            # merge elements from next potential heap into main heap
            # this happens q times across all loops
            # heappush after heappop ensures i < j
            # what you're adding are the new queries
            # that can be answered by reaching building i+1
            for element in query_store[i]:
                # log(q) complexity
                heappush(heap, element)

        return ans

    def leftmostBuildingQueries_naive(
        self, heights: List[int], queries: List[List[int]]
    ) -> List[int]:
        queries = [[i, j] if i < j else [j, i] for [i, j] in queries]
        m = len(heights)
        print(queries)

        ans = []
        for i, j in queries:
            for b in range(j, m):
                # print("i: ", i, "j: ", j, "b: ", b, "height: ", heights[b])
                if heights[i] <= heights[b] and heights[j] <= heights[b]:
                    ans.append(b)
                    break
            else:
                ans.append(-1)

        return ans


# @leet end


if __name__ == "__main__":
    h = [
        [6, 4, 8, 5, 2, 7],
        [5, 3, 8, 2, 6, 1, 4, 6],
        [1, 2],
    ]
    q = [
        [[0, 1], [0, 3], [2, 4], [4, 3], [2, 2]],
        [[0, 7], [3, 5], [5, 2], [3, 0], [1, 6]],
        [[0, 0], [0, 1], [1, 0], [1, 1]],
    ]
    e = [
        [2, 5, -1, 5, 2],
        [7, 6, -1, 4, 6],
        [0, 1, 1, 1],
    ]

    for i in range(0, len(h)):
        ai = Solution().leftmostBuildingQueries(h[i], q[i])
        print(i, ai == e[i])
