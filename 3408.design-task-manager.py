from typing import List
from heapq import heappush, heappop, heapify


# @leet start
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tmap = dict()
        for u, t, p in tasks:
            self.tmap[t] = (p, u)
        self.heap = [(-p, -t) for (_u, t, p) in tasks]
        heapify(self.heap)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heappush(self.heap, (-priority, -taskId))
        self.tmap[taskId] = (priority, userId)

    def edit(self, taskId: int, newPriority: int) -> None:
        heappush(self.heap, (-newPriority, -taskId))
        _, userId = self.tmap[taskId]
        self.tmap[taskId] = (newPriority, userId)

    def rmv(self, taskId: int) -> None:
        del self.tmap[taskId]

    def execTop(self) -> int:
        while self.heap:
            neg_p, neg_t = self.heap[0]
            if -neg_t in self.tmap:
                p, u = self.tmap[-neg_t]
                if p == -neg_p:
                    heappop(self.heap)
                    del self.tmap[-neg_t]
                    return u
            heappop(self.heap)

        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
# @leet end

