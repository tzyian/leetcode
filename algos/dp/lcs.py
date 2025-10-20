def lcs(a: str, b: str) -> str:
    m = len(a)
    n = len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct LCS,
    # Also same way done in shortest common supersequence
    lcs_length = dp[m][n]
    lcs_str = [""] * lcs_length
    i, j = m, n
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            lcs_str[lcs_length - 1] = a[i - 1]
            i -= 1
            j -= 1
            lcs_length -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs_str)


def lcs_patience(a: str, b: str) -> str:
    """Longest Common Subsequence using Patience Sorting and Binary Search
    Time Complexity: O((M + N) log(min(M, N)))
    Space Complexity: O(M + N)
    """
    from bisect import bisect_left

    # Step 1: Map characters in 'b' to their indices
    pos_map = {}
    for index, char in enumerate(b):
        if char not in pos_map:
            pos_map[char] = []
        pos_map[char].append(index)

    # Step 2: Create a list of positions in 'b' corresponding to characters in 'a'
    positions = []
    for char in a:
        if char in pos_map:
            positions.extend(reversed(pos_map[char]))

    # Step 3: Find the Longest Increasing Subsequence (LIS) in 'positions'
    lis = []
    predecessors = [-1] * len(positions)
    lis_indices = []

    for i, pos in enumerate(positions):
        idx = bisect_left(lis, pos)
        if idx == len(lis):
            lis.append(pos)
            lis_indices.append(i)
        else:
            lis[idx] = pos
            lis_indices[idx] = i
        if idx > 0:
            predecessors[i] = lis_indices[idx - 1]

    # Step 4: Reconstruct the LCS from the LIS
    lcs_length = len(lis)
    lcs_str = [""] * lcs_length
    k = lis_indices[-1]
    for i in range(lcs_length - 1, -1, -1):
        lcs_str[i] = a[positions[k]]
        k = predecessors[k]

    return "".join(lcs_str)
