// https://leetcode.com/problems/stone-game-ii

# Use dynamic programming: the states are (i, m) 
# for the answer of piles[i:] and that given m.

# with reference to the editorial
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        

        # player 1 is Alice, player -1 is Bob
        # returns the number of stones that alice gets
        @lru_cache(None)
        def f(player: bool, pileind: int, m: int) -> int:
            if pileind == n:
                return 0
            # if player is alice, initialise alicescore to low so max() works
            # vice versa if bob, high so min() works
            alicescore = -1 if player == 1 else 1000000
            stonestaken = 0
            
            # x is the number of piles she takes
            # piles she can take capped by 2m, or number of piles left, whichever is less
            for x in range(1, min(2 * m, n - pileind) + 1):
                stonestaken += piles[pileind + x - 1] # if she takes x piles
                if player == 1:
                    # find the max value alice can get out of all possible x
                    alicescore = max(alicescore, stonestaken + f(-player, pileind + x, max(m, x)))
                else: # bob wants to minimise alicescore
                    # find the min value alice can get out of all possible x
                    alicescore = min(alicescore, f(-player, pileind + x, max(m, x)))
            return alicescore


        return f(1, 0, 1)