# @leet start
from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        present = [0] * (n + 1)
        count = 0
        counts = [0] * n

        for i in range(n):
            ai = A[i]
            bi = B[i]
            present[ai] += 1
            present[bi] += 1

            if present[ai] == 2:
                count += 1
                present[ai] += 1
            if present[bi] == 2:
                count += 1
                present[bi] += 1
            counts[i] = count

        return counts

        
# @leet end
