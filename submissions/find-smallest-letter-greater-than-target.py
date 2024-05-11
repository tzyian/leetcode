// https://leetcode.com/problems/find-smallest-letter-greater-than-target

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        a=letters
        n = len(a)
        t=target
        l=0
        h=n-1
        while l<=h:
            m=l+(h-l)//2
            if a[m]<=t:
                l=m+1
            else:
                h=m-1
        if l==n:
            return a[0]
        return a[l]

