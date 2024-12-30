# @leet start

from math import trunc
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def eval(f):
            new = f(stack[-2], stack[-1])
            stack.pop()
            stack.pop()
            stack.append(new)

        stack = []

        for ele in tokens:
            match ele:
                case "+":
                    eval(lambda x, y: x + y)
                case "-":
                    eval(lambda x, y: x - y)
                case "*":
                    eval(lambda x, y: x * y)
                case "/":
                    eval(lambda x, y: trunc(x / y))
                case _:
                    stack.append(int(ele))

        return stack.pop()


# @leet end

