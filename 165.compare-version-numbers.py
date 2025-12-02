# @leet imports start
from typing import List

# @leet imports end

# @leet start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_parts = list(map(int, version1.split('.')))
        v2_parts = list(map(int, version2.split('.')))

        max_length = max(len(v1_parts), len(v2_parts))
        v1_parts.extend([0] * (max_length - len(v1_parts)))
        v2_parts.extend([0] * (max_length - len(v2_parts)))

        for part1, part2 in zip(v1_parts, v2_parts):
            if part1 > part2:
                return 1
            elif part1 < part2:
                return -1

        return 0
        
# @leet end
