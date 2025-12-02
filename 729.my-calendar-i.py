# @leet imports start
from typing import List, Optional

# @leet imports end


# @leet start
from dataclasses import dataclass
from typing import Self


@dataclass
class Node:
    start: int
    end: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None


class MyCalendar:
    def __init__(self):
        self.tree = None

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.tree:
            self.tree = Node(startTime, endTime)
            return True

        curr = self.tree
        new_node = Node(startTime, endTime)

        while curr:
            if startTime < curr.start:
                if endTime > curr.start:
                    return False
                elif curr.left:
                    curr = curr.left
                else:
                    curr.left = new_node
                    return True
            elif startTime == curr.start:
                return False
            elif startTime > curr.start:
                if startTime < curr.end:
                    return False
                elif curr.right:
                    curr = curr.right
                else:
                    curr.right = new_node
                    return True

        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
# @leet end

