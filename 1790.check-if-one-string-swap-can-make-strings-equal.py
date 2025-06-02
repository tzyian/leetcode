# @leet start
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        errors = 0
        e1 = ["", ""]
        e2 = ["", ""]
        n = len(s1)
        for i in range(n):
            if s1[i] != s2[i]:
                errors += 1

                if errors == 1:
                    e1[0] = s1[i]
                    e2[0] = s2[i]
                elif errors == 2:
                    e1[1] = s1[i]
                    e2[1] = s2[i]
                elif errors > 2:
                    return False

        ans = e1[0] == e2[1] and e1[1] == e2[0]
        print(errors, e1, e2)
        return ans

# @leet end
