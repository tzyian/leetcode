# @leet start
class Solution:
    def sortVowels(self, s: str) -> str:
        def is_vowel(c: str) -> bool:
            return c.lower() in ("a", "e", "i", "o", "u")

        vowels = sorted((c for c in s if is_vowel(c)), reverse=True)
        letters = (c if not is_vowel(c) else vowels.pop() for c in s)
        return "".join(letters)


# @leet end

x = Solution().sortVowels("lEetcOde")
print(x)

