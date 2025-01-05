# @leet start

from math import pow


class Solution:
    def myAtoi(self, s: str) -> int:
        def round(x: int) -> int:
            min_int = int(pow(-2, 31))
            max_int = int(pow(2, 31) - 1)
            if x < min_int:
                return min_int
            elif x > max_int:
                return max_int
            else:
                return x

        def read(ss: str, idx: int = 0, pos: bool = True) -> int:
            ls = []
            for i in range(idx, n):
                if ss[i].isnumeric():
                    ls.append(ss[i])
                else:
                    break
            ans_str = "".join(ls)
            if ans_str == "":
                return 0
            ans = int(ans_str)
            if not pos:
                ans = -ans

            return round(ans)

        ss = s.lstrip(" ")
        if not ss:
            return 0
        n = len(ss)
        match ss[0]:
            case "+":
                return read(ss, 1, True)
            case "-":
                return read(ss, 1, False)
            case _:
                return read(ss)


# @leet end
