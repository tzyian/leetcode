// https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters

from itertools import combinations
class Solution:
    def maxLength(self, arr: list[str]) -> int:
        n = len(arr)
        max_len = 0
        for i in range(n+1):
          for c in combinations(arr, i):
              s = "".join(c)
              if len(set(s)) == len(s):
                  max_len = max(max_len, len(s))
        return max_len