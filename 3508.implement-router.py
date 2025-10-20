# @leet imports start
from collections import defaultdict, deque
from typing import *

# @leet imports end

from bisect import bisect_left, bisect, bisect_right


# @leet start
class Router:

    def __init__(self, memoryLimit: int):
        # self.limit = memoryLimit
        self.router = deque(maxlen=memoryLimit)
        self.packets = set()
        self.dests = defaultdict(deque)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        item = (source, destination, timestamp)
        if item in self.packets:
            return False
        # if len(self.router) == self.limit:
        if len(self.router) == self.router.maxlen:
            self.forwardPacket()

        self.router.append(item)
        self.packets.add(item)
        self.dests[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.router:
            return []
        s, d, t = self.router.popleft()
        self.packets.remove((s, d, t))
        self.dests[d].popleft()
        return [s, d, t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        q = self.dests[destination]
        # left = bisect_left(q, startTime, key=lambda i: i[2])
        # right = bisect_right(q, endTime, key=lambda i: i[2])
        left = bisect_left(q, startTime)
        right = bisect_right(q, endTime)
        return right - left


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
# @leet end

calls = [
    "Router",
    "addPacket",
    "addPacket",
    "addPacket",
    "addPacket",
    "addPacket",
    "forwardPacket",
    "addPacket",
    "getCount",
]
args = [
    [3],
    [1, 4, 90],
    [2, 5, 90],
    [1, 4, 90],
    [3, 5, 95],
    [4, 5, 105],
    [],
    [5, 2, 110],
    [5, 100, 110],
]
for call, arg in zip(calls, args):
    if call == "Router":
        obj = Router(*arg)
    elif call == "addPacket":
        print(obj.addPacket(*arg))
    elif call == "forwardPacket":
        print(obj.forwardPacket())
    elif call == "getCount":
        print(obj.getCount(*arg))

