// https://leetcode.com/problems/word-break

from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordDict = wordDict
        return self.helper(s)
    
    @cache
    def helper(self, s: str) -> bool:
        curr_word = ""
        for i in range(len(s)):
            curr_word += s[i]
            is_alr_word = False
            
            if curr_word in self.wordDict:
                is_alr_word = True

            if not is_alr_word and curr_word not in self.wordDict:
                continue

            check_new_word = self.helper(s[i+1:])
            if check_new_word:
                return True

            # if not is_alr_word and curr_word in self.wordDict: N Y
            #     # a word has been found
            #     is_alr_word = True
            #     # either continue adding or check new word 
            #     new = self.helper(s[i+1:])
            #     if new:
            #         return new
            # elif is_alr_word and curr_word in self.wordDict: Y Y
            #     new = self.helper(s[i+1:])
            #     if new:
            #         return new

            # elif is_alr_word and curr_word not in self.wordDict:  Y N
            #     # check new word
            #     new = self.helper(s[i+1:])
            #     if new:
            #         return new
            


        return curr_word in self.wordDict

