# @leet start
from collections import defaultdict
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        neg = defaultdict(int)
        pos = defaultdict(int)
        zeros = 0

        for x in nums:
            if x < 0:
                neg[x] += 1
            elif x > 0:
                pos[x] += 1
            else:
                zeros += 1

        r = []

        if zeros:
            for n in neg:
                if -n in pos:
                    r.append((0, n, -n))

            if zeros > 2:
                r.append((0, 0, 0))

        for set_a, set_b in ((neg, pos), (pos, neg)):
            set_a_items = list(set_a.items())
            for i, (x, q) in enumerate(set_a_items):
                for x2, q2 in set_a_items[i:]:
                    if x != x2 or (x == x2 and q > 1):
                        if -x - x2 in set_b:
                            r.append((x, x2, -x - x2))

        return r

    def threeSumTLE2(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        triplets = set()
        pairs = set()
        vals = defaultdict(list[int])

        for i in range(n):
            for j in range(i + 1, n):
                ele0 = nums[i]
                ele1 = nums[j]

                if ele0 < ele1:
                    if (ele0, ele1) in pairs:
                        continue
                    vals[-nums[i] - nums[j]].append((i, j))
                    pairs.add((ele0, ele1))
                else:
                    if (ele0, ele1) in pairs:
                        continue
                    vals[-nums[i] - nums[j]].append((i, j))
                    pairs.add((ele1, ele0))

        for k, ele in enumerate(nums):
            if ele in vals:
                for i, j in vals[ele]:
                    if k <= j:
                        continue

                    triplets.add(tuple(sorted([nums[i], nums[j], nums[k]])))

        return list(triplets)

    def threeSumTLE(self, nums: List[int]) -> List[List[int]]:
        # O(n^2), O(n^2)
        n = len(nums)
        triplets = set()
        vals = defaultdict(list[int])

        for i in range(n):
            for j in range(i + 1, n):
                vals[-nums[i] - nums[j]].append((i, j))

        for k, ele in enumerate(nums):
            if ele in vals:
                for i, j in vals[ele]:
                    if k <= j:
                        continue

                    triplets.add(tuple(sorted([nums[i], nums[j], nums[k]])))

        return list(triplets)


# @leet end

n1 = [-1, 0, 1, 2, -1, -4]
n2 = [0, 0, 0]
x = Solution().threeSum(n1)
print(x)
