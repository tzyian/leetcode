def best_price(price: list[int]) -> int:
    n = len(price)
    dp = [0] * (n + 1)

    # if the total length of the rod is i
    for i in range(1, n + 1):
        # piece of length j is cut
        # if j == i, then no cut is made
        # cut at length j, then use the subproblem of length i-j
        for j in range(1, i + 1):
            dp[i] = max(dp[i], price[j - 1] + dp[i - j])

    return dp[n]
