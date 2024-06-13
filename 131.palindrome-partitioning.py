# @leet start
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []

        def backtrack(start: int, curr: list[str]) -> None:
            if curr and start == n:
                ans.append(curr[:])
            for i in range(start, n):
                if is_palindrome(start, i):
                    curr.append(s[start : i + 1])
                    backtrack(i + 1, curr)
                    curr.pop()

        def is_palindrome(start: int, stop: int) -> bool:
            diff = stop - start + 1
            for i in range(diff):
                if s[start + i] != s[stop - i]:
                    return False
            return True

        backtrack(0, [])

        return ans


# @leet end
if __name__ == "__main__":
    testcases = ["aab", "a"]
    for tc in testcases:
        sn = Solution().partition(tc)
        print(tc, sn)
