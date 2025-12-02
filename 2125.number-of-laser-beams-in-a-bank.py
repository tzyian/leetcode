# @leet imports start
from typing import List, Optional

# @leet imports end


# @leet start
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        n = len(bank)
        beams = 0
        prev = 0
        for i in range(n):
            devices = bank[i].count("1")
            beams += devices * prev

            if devices != 0:
                prev = devices

        return beams


# @leet end

