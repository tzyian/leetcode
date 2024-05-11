// https://leetcode.com/problems/compare-version-numbers

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        vers1 = version1.split(".")
        vers2 = version2.split(".")

        l1 = len(vers1)
        l2 = len(vers2)

        # make vers1 the shorter one
        if l1 > l2:
            return -self.compareVersion(version2, version1)

        for i in range(len(vers1)):
            v1 = int(vers1[i])
            v2 = int(vers2[i])
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1

        for j in range(l1, l2):
            print(j, vers2[j])
            if int(vers2[j]) > 0:
                return -1

        return 0


x = Solution().compareVersion("1", "1.00.01.000")
print(x)