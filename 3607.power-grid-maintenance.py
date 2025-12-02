# @leet imports start
from collections import defaultdict
from heapq import heapify, heappop
from typing import List

# @leet imports end


# @leet start
class Solution:
    def processQueries(
        self, c: int, connections: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        UF = dict()

        def union(x: int, y: int) -> None:
            rootX = find(x)
            rootY = find(y)
            UF[rootX] = rootY

        def find(x: int) -> int:
            if x not in UF:
                UF[x] = x
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]

        offline = set()

        # parse grid
        for u, v in connections:
            union(u, v)
        for i in range(1, c + 1):
            find(i)

        groups = defaultdict(list)
        for i in range(1, c + 1):
            groups[UF[i]].append(i)

        for group in groups.values():
            heapify(group)

        def check_station(stn_id: int) -> int:
            if stn_id not in offline:
                return stn_id

            grp = groups[UF[stn_id]]

            while grp and grp[0] in offline:
                heappop(grp)

            if not grp:
                return -1
            return grp[0]

        # resolve queries
        ans = []
        for [t, x] in queries:
            if t == 2:
                offline.add(x)
            else:
                id = check_station(x)
                ans.append(id)
        return ans


# @leet end

