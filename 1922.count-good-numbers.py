# @leet start
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # there are 4 prime digits for odd indices
        # there are (0 2 4 6 8) 5 even digits for even indices

        MOD = 10**9 + 7

        num_odds = n // 2
        num_evens = n - num_odds

        def fast_exp(base: int, pow: int) -> int:
            res = 1
            mult = base
            while pow > 0:
                if pow & 1 == 1:
                    res = res * mult % MOD
                mult = mult * mult % MOD
                pow //= 2
            return res

        return (fast_exp(4, num_odds) * fast_exp(5, num_evens)) % MOD


# @leet end

