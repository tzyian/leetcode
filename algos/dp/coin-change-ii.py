# Number of combinations that make up a certain amount using given coin denominations


def coin_change_2(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1  # There's one way to make amount 0: use no coins

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] += dp[x - coin]

    return dp[amount]
