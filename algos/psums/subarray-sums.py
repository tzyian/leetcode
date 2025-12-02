from collections import defaultdict
from typing import List, Optional

"""
Use prefix sums mod k.
If two prefixes have the same remainder r, their difference is divisible by k;
ensure the gap is at least 2.

523. Continuous Subarray Sum
560. Subarray Sums Equals K
974. Subarray Sums Divisible By K
    index by modulus
1590. Make Sum Divisible by P
    modular arithmetic
3381. Maximum Subarray Sum With Length Divisible by K: 
    instead of finding max array starting at i, find max array ending at i and prefix. Then do dp
"""

# subsums[0] = -1, meaning prefix sum before index 0 has remainder 0.
# if psum % k == 0,
# prefix[i] − prefix[−1]
# (i.e., sum of nums[0..i]) divisible by k.

# An easier way to think about it is:
# If the psum is divisible by k, then all the nums up to now is the ans
# So index + 1 cos 0-indexed


def subarraysDivByK(nums: List[int], k: int) -> int:
    # 974. Subarray Sums Divisible By K
    counts = defaultdict(int)
    counts[0] = 1
    ans = 0
    psum = 0
    for x in nums:
        psum += x
        ans += counts[psum % k]
        counts[psum % k] += 1

    return ans


def minSubarray(nums: List[int], p: int) -> int:
    # 1590. Make Sum Divisible by P
    # the array is of the form      px + k, where 0 <= k < p
    # remove the smallest subarray of form     py + k

    # let sum(L,R) = Sr - Sl
    # Ti = Si mod p    # (i.e. Ti = Si % p)
    # Si ≡ Ti (mod p)  # (p | Si - Ti)
    # Ti ≡ Si (mod p)  # by symmetry

    # sum(L,R) = Sr - Sl
    # by definition, sum(L,R) ≡ Sr - Sl (mod p)
    # Sr ≡ Tr (mod p)
    # Sl ≡ Tl (mod p)
    # by modular subtraction,
    # Sr - Sl ≡ Tr - Tl (mod p)

    # sum(L,R) ≡ Tr - Tl ≡ Sr - Sl (mod p)
    # i.e. Sr - Sl and Tr - Tl have the same remainder
    # we want Sr - Sl ≡ k (mod p)
    # Tr - Tl ≡ k (mod p)
    # Tl ≡ Tr - k (mod p)

    n = len(nums)
    tot = sum(nums)
    k = tot % p
    if k == 0:
        return 0

    hmap = dict()
    hmap[0] = -1

    inf = 10**9 + 7
    min_dist = inf
    psum = 0
    for i, x in enumerate(nums):
        psum += x
        ti = psum % p
        needed = ((ti - k) % p + p) % p
        if needed in hmap:
            dist = i - hmap[needed]
            min_dist = min(dist, min_dist)
        hmap[ti] = i

    if min_dist == n:
        return -1
    return min_dist


def maxSubarraySum(nums: List[int], k: int) -> int:
    # 3381. Maximum Subarray Sum With Length Divisible by K
    # The key idea is to inverse.
    # Rather the finding the maximum subarray that starts at i
    # Find the maximum subarray that ends at i
    # (i.e. find the minimum prefix to subtract)

    # element is indexed by its position % k

    # lol this question must accommodate +-10**(5+9)
    inf = 10**20 + 7

    best = -inf
    dp = [inf] * k
    dp[k - 1] = 0

    psum = 0
    for i, x in enumerate(nums):
        psum += x
        r = i % k

        if i >= k - 1:
            best = max(best, psum - dp[r])
        dp[r] = min(dp[r], psum)

    return best
