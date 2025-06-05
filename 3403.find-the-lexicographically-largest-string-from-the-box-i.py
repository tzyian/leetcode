# @leet start
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        # the lexicographically largest string picks the largest lexico character
        # as always there's brute force n^2 solution
        # other than the largest, each of numFriends-1 has 1 character
        # actually no that is wrong, eg 312,33 has 33 larger
        # 1 2 | 3 2 1 | * 3 2 3 | 3 2 2
        # iterate through, take the indexes of the largest numbers
        # how to compare concurrently between 3 substrings though
        # use a trie??? then just iterate the trie at the end

        # if the string is 3 3 3 3 3 3 it will still be n^2 time
        # Hint: Find lexicographically largest substring of size n - numFriends + 1 or less starting at every index.
        # I guess you could rolling hash this (not bsearch though) but seems complicated

        """
        https://leetcode.com/problems/last-substring-in-lexicographical-order/solutions/363662/short-python-code-o-n-time-and-o-1-space-with-proof-and-visualization/comments/383861/
        """

        n = len(word)

        def last_substring(s: str) -> str:
            i = 0
            j = 1
            k = 0
            while j + k < n:
                # if current index of 2 substrings are equal
                # just carry on
                if s[i + k] == s[j + k]:
                    k += 1
                    continue

                # if si is lexico larger, then restart j
                elif s[i + k] > s[j + k]:
                    j = j + k + 1

                # si is lexico smaller, so restart, similar to i, j = 0, 1
                # from the next letter onwards
                # max() because for any i < x < j, x will have already been checked,
                # so x cannot be the start of a new lexixo string
                else:
                    i = max(i + k + 1, j)
                    j = i + 1
                # reset k to initial indices
                k = 0
            return s[i:]

        if numFriends == 1:
            return word

        last = last_substring(word)
        m = len(last)
        # if too many friends left, then n-numfriends+1. Else m.
        return last[: min(m, n - numFriends + 1)]


# @leet end

s = "dbca"
ns = 2
x = Solution().answerString(s, ns)
print(x)

s = "gggg"
ns = 4
x = Solution().answerString(s, ns)
print(x)

