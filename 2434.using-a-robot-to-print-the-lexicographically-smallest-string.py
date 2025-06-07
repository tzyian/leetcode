from collections import Counter


# @leet start
class Solution:
    def robotWithString(self, s: str) -> str:
        # for every char in s
        # 1. add to a stack
        # 2. at any point in time, pop the stack and add to ans
        # if a char is the minimum in the string, it must be the first char
        # bbbaca -> aacbbb
        # ...azzzzaazzz ->

        # to redo...

        ctr = Counter(s)
        lo = "a"
        ans = []
        stack = []
        for c in s:
            stack += c
            ctr[c] -= 1
            while lo < "z" and ctr[lo] == 0:
                lo = chr(ord(lo) + 1)
            while stack and stack[-1] <= lo:
                ans.append(stack.pop())
        return "".join(ans)

        # def to_i(x: str) -> int:
        #     return ord(x) - ord("a")
        #
        # NUM_ALPHA = 26
        # ans = []
        # ctr = [0] * NUM_ALPHA
        # stack = []
        # n = len(s)
        # j = 0
        #
        # for c in s:
        #     ctr[ord(c) - ord("a")] += 1
        #
        # next_char = 0
        # for i in range(n):
        #     while j < NUM_ALPHA:
        #         if ctr[j] > 0:
        #             next_char = j
        #             break
        #         j += 1
        #
        #     ci_ind = to_i(s[i])
        #     if ci_ind == next_char:
        #         ctr[next_char] -= 1
        #         ans.append(s[i])
        #         # if ctr[ci_ind] == 0:
        #         #     j += 1
        #
        #     if stack and to_i(stack[-1]) == next_char:
        #         ans.append(stack.pop())
        #
        #     else:
        #         stack.append(s[i])
        #         ctr[ci_ind] -= 1
        #
        # ans.extend(reversed(stack))
        #
        # return "".join(ans)


# @leet end

s = "zza"
s = "bac"
s = "bbbaca"
x = Solution().robotWithString(s)
print(x)
