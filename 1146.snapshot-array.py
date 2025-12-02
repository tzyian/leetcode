# @leet imports start
from typing import List, Optional

# @leet imports end

# @leet start
class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.arr = [{} for _ in range(length)]
        

    def set(self, index: int, val: int) -> None:
        self.arr[index][self.snap_id] = val
        

    def snap(self) -> int:
        self.snap_id += 1
        

    def get(self, index: int, snap_id: int) -> int:
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
# @leet end
