# @leet start


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        NUM_ALPHA = 26

        cr = lambda x: ord(x) - ord("a")
        starts = [-1] * NUM_ALPHA
        lasts = [-1] * NUM_ALPHA
        for i, c in enumerate(s):
            c = cr(c)
            if starts[c] == -1:
                starts[c] = i
            lasts[c] = i

        ans = 0
        for i in range(NUM_ALPHA):
            first = starts[i]
            last = lasts[i]
            unqs = set()
            for j in range(first + 1, last):
                unqs.add(s[j])
            ans += len(unqs)

        return ans


# @leet end
