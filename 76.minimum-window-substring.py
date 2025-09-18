# @leet start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        # 2 ptr O(n) soln

        best_l, best_r = 0, inf
        l, r = 0, 0
        hit = set()  # hit is the letters that have hit target frequency
        c = Counter(t)
        d = defaultdict(int)  # freq of letters encountered
        for r, ch in enumerate(s):
            if ch in c:
                d[ch] += 1
                if d[ch] >= c[ch]:
                    hit.add(ch)
            # while all targets met, move left ptr
            while len(hit) == len(c):
                if r - l < best_r - best_l:
                    best_l = l
                    best_r = r
                cl = s[l]
                l += 1
                if cl in c:
                    d[cl] -= 1
                    if d[cl] < c[cl]:
                        hit.remove(cl)
        if best_r == inf:
            return ""
        else:
            return s[best_l : best_r + 1]


# @leet end

s = "ADOBECODEBANC"
t = "ABC"
x = Solution().minWindow(s, t)
print(x)


s = "a"
t = "a"
x = Solution().minWindow(s, t)
print(x)


s = "a"
t = "aa"
x = Solution().minWindow(s, t)
print(x)
