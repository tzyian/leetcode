from typing import List


# @leet start


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def transform(word: str) -> str:
            vowels = ("a", "e", "i", "o", "u")
            tf = []
            for c in word:
                c = c.lower()
                if c in vowels:
                    tf.append("#")
                else:
                    tf.append(c)

            return "".join(tf)

        seen = dict()
        exacts = set()
        for word in wordlist:
            exacts.add(word)

            if word.lower() not in seen:
                seen[word.lower()] = word

            tf = transform(word)
            if tf not in seen:
                seen[tf] = word

        ans = []
        for query in queries:

            if query in exacts:
                ans.append(query)
            elif query.lower() in seen:
                ans.append(seen[query.lower()])
            elif transform(query) in seen:
                ans.append(seen[transform(query)])
            else:
                ans.append("")

        return ans


# @leet end

w = ["KiTe", "kite", "hare", "Hare"]
q = ["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"]
exp = ["kite", "KiTe", "KiTe", "Hare", "hare", "", "", "KiTe", "", "KiTe"]
x = Solution().spellchecker(w, q)
print(x)
assert x == exp

["yellow"]
["YellOw"]

