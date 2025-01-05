# @leet start
from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        atoi = lambda x: ord(x) - ord("a")
        itoa = lambda x: chr(x + ord("a"))
        BACKWARD = 0
        FORWARD = 1

        n = len(s)

        s_ls = list(s)
        int_ls = [atoi(x) for x in s_ls]
        diffs = [0] * n

        for i, j, dir in shifts:
            d = 1 if dir == BACKWARD else -1
            if i > 0:
                diffs[i - 1] += d
            diffs[j] -= d

            # match dir:
            #     case BACKWARD:
            #         if i > 0:
            #             diffs[i - 1] += 1
            #         diffs[j] -= 1
            #
            #     case FORWARD:
            #         if i > 0:
            #             diffs[i - 1] -= 1
            #         diffs[j] += 1

        ansi = [0] * n
        consec = 0

        for i in range(n - 1, -1, -1):
            consec += diffs[i]
            ansi[i] = (consec + int_ls[i]) % 26

        ans = "".join(itoa(x) for x in ansi)
        return ans


# @leet end
