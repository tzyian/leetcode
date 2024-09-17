# @leet start


class Solution:
    def reverseParentheses(self, s: str) -> str:
        """
        TC O(n)
        SC O(n) because storing dicts for fwd/back pairs
        """
        n = len(s)
        stack = []
        pairs = {}

        # Get the bracket pairs
        for i in range(n):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                begin = stack.pop()
                pairs[i] = begin
                pairs[begin] = i

        # Start the reverse mode
        ans_arr = []
        dir = 1
        j = 0

        while j >= 0 and j < n:
            if s[j] == "()":
                j = pairs[j]
                dir = -dir
            else:
                ans_arr.append(s[j])
            j += dir

        return "".join(ans_arr)


# @leet end
def reverseParenthesesNSquared(s: str) -> str:
    def swap(s: list, a: int, b: int) -> None:
        s[a], s[b] = s[b], s[a]

    n = len(s)
    ans_arr = [c for c in s]
    stack = []

    for i in range(n):
        if s[i] == "(":
            stack.append(i + 1)
        elif s[i] == ")":
            begin = stack.pop()
            end = i - 1
            length = end - begin + 1
            for j in range(length // 2):
                swap(ans_arr, begin + j, end - j)

    ans = []
    for c in ans_arr:
        if c != ")" and c != "(":
            ans.append(c)
    return "".join(ans)


s1 = "(ab(c(de)f))(abcde)"
res = Solution().reverseParentheses(s1)
print(res)
