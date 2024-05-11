// https://leetcode.com/problems/stone-game-iii

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        

        from functools import lru_cache
        @lru_cache(None)
        # 1 is alice, -1 is bob
        def f(player, pileind):
            if pileind >= n:
                return 0
            alicescore = -10000 if player == 1 else 100000
            stonesum = 0
            for x in range(1, min(n - pileind, 3) + 1):
                stonesum += stoneValue[pileind + x - 1]
                if player == 1: # Alice
                    alicescore = max(alicescore, stonesum + f(-player, pileind + x))
                elif player == -1: # Bob
                    alicescore = min(alicescore, f(-player, pileind + x))
            return alicescore       

        
        alicescore = f(1, 0)

        bobscore = sum(stoneValue) - alicescore
        if bobscore == alicescore:
            return "Tie"
        elif bobscore > alicescore:
            return "Bob"
        else:
            return "Alice"



