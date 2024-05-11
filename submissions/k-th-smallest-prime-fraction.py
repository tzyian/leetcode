// https://leetcode.com/problems/k-th-smallest-prime-fraction

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        left: float = 0.0
        right: float = 1.0
        
        while left < right:
            mid = (left + right) / 2
            max_frac = 0.0
            num_smaller = 0
            numer_idx = 0
            denom_idx = 0
            j = 1 # first possible index of denominator, since numerator starts at 0

            # num of fractions smaller than mid
            for i in range(n - 1): # up to 2nd last element
                while j < n and arr[i] >= mid * arr[j]:
                    # arr[i] / arr[j] >= mid
                    # given numerator i and denom j, the first k denominators are bigger than mid
                    # Because of the triangle shape ◥,
                    j += 1
                
                num_smaller += n - j

                # no more fractions
                if j == n:
                    break
                
                frac = arr[i] / arr[j]

                if frac > max_frac:
                    numer_idx = i
                    denom_idx = j
                    max_frac = frac
            if num_smaller == k:
                return arr[numer_idx], arr[denom_idx]
            elif num_smaller > k:
                right = mid
            else:
                left = mid



        
        