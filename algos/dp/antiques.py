# Problem: Given a budget and a list of antique types with their prices and quality values,
# determine the maximum total quality value that can be obtained by purchasing antiques
# without exceeding the budget. The cost of buying k copies of an antique type i is k^2 * price[i],
# and the quality value obtained is k * quality[i].


def antiques(budget: int, price: list[int], quality: list[int]) -> int:
    n = len(price)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # Iterate through each antique type i (1-indexed)
    for i in range(1, n + 1):
        p_i = price[i]
        q_i = quality[i]

        # Iterate through each possible budget j
        for j in range(budget + 1):
            # Initialize current state with the case where we buy 0 copies of type i
            # This is simply the value from the previous type with the same budget.
            max_val = dp[i - 1][j]

            # Iterate through possible copies k (1, 2, 3...)
            k = 1
            while True:
                cost_k = k * k * p_i
                val_k = k * q_i

                # Stop if cost exceeds current budget j
                if cost_k > j:
                    break

                # Transition
                remaining_budget = j - cost_k
                current_happiness = dp[i - 1][remaining_budget] + val_k

                if current_happiness > max_val:
                    max_val = current_happiness

                k += 1

            dp[i][j] = max_val

    return dp[n][budget]
