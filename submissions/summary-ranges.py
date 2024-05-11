// https://leetcode.com/problems/summary-ranges

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        ans = []
        if n == 0:
            return ans
        if n == 1:
            ans.append(str(nums[0]))
            return ans

        i = 0
        while i < n:
            j = i
            while j + 1 < n and nums[j + 1] == nums[j] + 1:
                j += 1
            if i == j:
                r = str(nums[i])
                ans.append(r)
            else:
                r = f"{str(nums[i])}->{str(nums[j])}"
                ans.append(r)
            i = j + 1
        return ans

         


        