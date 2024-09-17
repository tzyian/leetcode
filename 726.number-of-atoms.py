"""
A tidier variant can be found at e.g. https://leetcode.com/problems/number-of-atoms/solutions/140802/python-20-lines-very-readable-simplest-and-shortest-solution-36-ms-beats-100/?envType=daily-question&envId=2024-07-14

There can also be the recursive descent parsing algorithm (see editorial)
"""

# @leet start
from collections import Counter


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        atoms = Counter()
        mult_stack = [1]
        prefix_mults = [1]  # actually just pop and divide will be sufficient

        i = n - 1
        while i >= 0:
            c = formula[i]
            if c.isnumeric():
                num = []
                while i >= 0 and formula[i].isnumeric():
                    num += formula[i]
                    i -= 1
                mult_stack[-1] = int("".join(num[::-1]))

            elif c.isalpha() and c.isupper():
                atoms[c] += mult_stack[-1] * prefix_mults[-1]
                mult_stack[-1] = 1
                i -= 1
            elif c.isalpha() and c.islower():
                element = []
                while i >= 0 and formula[i].isalpha():
                    element.append(formula[i])
                    if formula[i].isupper():
                        i -= 1
                        break
                    i -= 1

                element = "".join(element[::-1])
                atoms[element] += mult_stack[-1] * prefix_mults[-1]
                mult_stack[-1] = 1

            elif c == ")":
                prefix_mults.append(prefix_mults[-1] * mult_stack[-1])
                mult_stack.append(1)
                i -= 1
            elif c == "(":
                mult_stack.pop()
                prefix_mults.pop()
                mult_stack[-1] = 1
                i -= 1
        # print(atoms)
        ans = []
        for k, v in sorted(atoms.items()):
            if v > 1:
                ans.append(k + str(v))
            else:
                ans.append(k)
        return "".join(ans)

    # @leet end


s = "Ab2Cd2(E2(FG3)4)5"
x = Solution().countOfAtoms(s)
print(x, "A2b2C2d2E10F8G60")

inputs = ["H2O", "Mg(OH)2", "K4(ON(SO3)2)2", "Ab2Cd2(E2(FG3)4)5"]
expected = ["H2O", "H2MgO2", "K4N2O14S4", "Ab2Cd2E10F20G60"]
for i in range(len(inputs)):
    # if i != 1:
    #     continue
    x = Solution().countOfAtoms(inputs[i])
    print(x, expected[i])
    assert x == expected[i]
