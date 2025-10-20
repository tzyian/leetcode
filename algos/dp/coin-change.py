# Minimum number of coins to make amount


def coin_change(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make amount 0

    # Iterate through each coin
    for coin in coins:
        # Update the dp array for all amounts that can be reached with the current coin
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    # If dp[amount] is still infinity, it means it's not possible to make that amount
    return dp[amount] if dp[amount] != float("inf") else -1
