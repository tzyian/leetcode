// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
              
        for i in range(len(s)):
            match s[i]:
                case "(":
                    stack.append("(")
                case ")":
                    if len(stack) == 0 or stack[-1] != "(":
                        return False
                    stack.pop()
                case "[":
                    stack.append("[")
                case "]":
                    if len(stack) == 0 or stack[-1] != "[":
                        return False
                    stack.pop()
                case "{":
                    stack.append("{")
                case "}":
                    if len(stack) == 0 or stack[-1] != "{":
                        return False
                    stack.pop()
        return len(stack) == 0
    
                