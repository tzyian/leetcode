// https://leetcode.com/problems/time-needed-to-inform-all-employees

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # construct tree
        graph = [[] for _ in range(n)]
        for emplee, mgr in enumerate(manager):
            if mgr == -1:
                continue
            graph[mgr].append(emplee)
        

        timetaken = [0 for _ in range(n)]
        stack = []
        informed = set()
        stack.append(headID)
        while stack:
            curr = stack.pop()
            if curr not in informed:
                informed.add(curr)
                for i in graph[curr]:
                    timetaken[i] = informTime[curr] + timetaken[i] + timetaken[curr]
                    stack.append(i)
        print(timetaken)
        return max(timetaken)

        