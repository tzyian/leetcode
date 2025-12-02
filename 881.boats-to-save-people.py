# @leet imports start
from typing import List, Optional

# @leet imports end


# @leet start
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        l = 0
        r = n - 1
        ans = 0
        while l <= r:
            if l == r:
                return ans + 1
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            ans += 1
        return ans


# @leet end

