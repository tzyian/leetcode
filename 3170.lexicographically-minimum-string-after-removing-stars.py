from collections import deque


# @leet start
class Solution:
    def clearStars(self, s: str) -> str:
        # az...zazzz*
        # dont you always delete the leftmost * and the closest char???
        # i guess just how to do it the fastest... without using a double linked i guess
        # ok the below simulation is O(n^2) and will probably TLE
        # nvm i failed to get lexico smallest char before i
        # use a heap or sth
        # NOTE: not working, see java

        def to_i(x: str) -> int:
            return ord(x) - ord("a")

        dq = deque(s)
        ctr = [0] * 26
        n = len(s)
        for c in s:
            if c == "*":
                continue
            ctr[to_i(c)] += 1

        smallest_char = 0

        i = 0
        while i < n:
            if dq[i] == "*":
                j = i - 1
                del dq[i]

                while ctr[smallest_char] == 0:
                    smallest_char += 1
                ctr[smallest_char] -= 1

                while to_i(dq[j]) != smallest_char:
                    j -= 1
                del dq[j]

                i -= 2
                n -= 2
            i += 1

        ans_ls = list(dq)
        return "".join(ans_ls)


# @leet end
l = "aaba*"
l = "aaazzzzzzzzzzzzzzzzzb*zzzzzba*"
l = "d*c"
x = Solution().clearStars(l)
print(x)

