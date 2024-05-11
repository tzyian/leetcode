// https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if digits == "":
            return []

        map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        ans = []
        for c in digits:
            if len(ans) == 0:
                for x in map[c]:
                    ans.append(x)
            else:
                tmp = []
                for x in ans:
                    for y in map[c]:
                        tmp.append(x + y)
                ans = tmp

        return ans