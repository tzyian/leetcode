# @leet start
from heapq import heappop, heappush

Heap = list[int]


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # this looks like union find but I have no idea how to code that

        # NOTE: one way doesn't work cos if r->k, and later r->s, then you never know that s->k
        # yeah as shown, doesn't work on test case 1
        # no way to do pointers or references either
        # cos you still need to reassign pointers or references
        n = len(s1)

        dc = dict()
        for i in range(n):
            c1 = s1[i]
            c2 = s2[i]
            if c1 < c2:
                dc[c1] = c1
                dc[c2] = c1
            else:
                dc[c2] = c2
                dc[c1] = c2

        ans = []
        for c in baseStr:
            curr = c
            prev = c
            while dc[curr] != curr:
                curr = dc[curr]
                dc[prev] = dc[curr]
                prev = dc[curr]
            ans.append(curr)

        return "".join(ans)


# @leet end
s1 = "parker"
s2 = "morris"
baseStr = "parser"
x = Solution().smallestEquivalentString(s1, s2, baseStr)
print(x)

