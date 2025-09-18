from typing import List


# @leet start
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:

        a = 0
        b = 0
        tens = 1
        while n > 0:
            rem = n % 10
            if rem == 0:
                # borrow from tens place
                a += 5 * tens
                b += 5 * tens
                n -= 10
            elif n > 10 and rem == 1:
                # n > 10 prevents 1 from being split into 55 and 56
                # borrow from tens place
                a += 5 * tens
                b += 6 * tens
                n -= 10
            else:
                a += (rem // 2) * tens
                b += (rem - rem // 2) * tens
            tens *= 10
            n //= 10

        return [a, b]


# @leet end

