def knapsack(W: int, val: list[int], wt: list[int]) -> int:
    """
    Solve the 0/1 Knapsack problem using dynamic programming.
    W (int): Maximum weight capacity of the knapsack.
    val (list): List of values of the items.
    wt (list): List of weights of the items.
    """

    n = len(wt)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    # dp[i][j] is up to ith item with j capacity
    for i in range(n + 1):
        for j in range(W + 1):
            # If there is no item or the knapsack's capacity is 0
            if i == 0 or j == 0:
                dp[i][j] = 0
            else:
                pick = 0

                # Pick ith item if it does not exceed the capacity of knapsack
                if wt[i - 1] <= j:
                    pick = val[i - 1] + dp[i - 1][j - wt[i - 1]]

                # Don't pick the ith item
                notPick = dp[i - 1][j]

                dp[i][j] = max(pick, notPick)

    return dp[n][W]


def knapsackSpaceOpt(W, val, wt):
    # Initializing dp list
    dp = [0] * (W + 1)

    # Taking first i elements
    for i in range(1, len(wt) + 1):
        # Starting from back, so that we also have data of
        # previous computation of i-1 items
        for j in range(W, wt[i - 1] - 1, -1):
            dp[j] = max(dp[j], dp[j - wt[i - 1]] + val[i - 1])

    return dp[W]
