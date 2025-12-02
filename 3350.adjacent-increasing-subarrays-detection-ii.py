# @leet imports start
from typing import List, Optional

# @leet imports end


# @leet start
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        # if can find 2, then return k*2
        # else return 1 or k // 2
        ans = 1
        n = len(nums)

        i = 0
        cont = 1

        while i < n:
            j = i + 1
            cont2 = 1
            while j < n:
                if nums[j] > nums[j - 1]:
                    j += 1
                    cont2 += 1
                else:
                    break

            ans = max(ans, cont2 // 2, min(cont2, cont))
            cont = cont2
            i = j

        return ans


# @leet end

nums = [2, 5, 7, 8, 9, 2, 3, 4, 3, 1]
x = Solution().maxIncreasingSubarrays(nums)
print(x)

nums = [1, 2, 3, 4, 4, 4, 4, 5, 6, 7]
x = Solution().maxIncreasingSubarrays(nums)
print(x)

