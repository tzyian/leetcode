// https://leetcode.com/problems/new-21-game

'''
Qn
score = 0
while score < k:
    score += random.randInt(1, maxPts + 1)
return probability score <= n


REDO!!! Copied answer from editorial

Also go look up this video https://youtu.be/zKi4LzjK27k


'''



class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0] * (n + 1)
        dp[0] = 1
        s = 1 if k > 0 else 0
        for i in range(1, n + 1):
            dp[i] = s / maxPts
            if i < k:
                s += dp[i]
            if i - maxPts >= 0 and i - maxPts < k:
                s -= dp[i - maxPts]
        return sum(dp[k:])
