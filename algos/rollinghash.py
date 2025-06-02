def compute_hash(s, B, M):
    h = 0
    for c in s:
        h = (h * B + ord(c)) % M
    return h

def rolling_hash(text, window_size, B=256, M=10**9 + 7):
    n = len(text)
    if n < window_size:
        return []

    # Compute B^(window_size - 1) % M for use in removing leading char
    B_power = 1
    for _ in range(window_size - 1):
        B_power = (B_power * B) % M

    hashes = []
    # First window hash
    h = compute_hash(text[:window_size], B, M)
    hashes.append(h)

    for i in range(1, n - window_size + 1):
        left = ord(text[i - 1])
        right = ord(text[i + window_size - 1])

        # Remove leftmost char, add rightmost char
        h = (h - left * B_power) % M
        h = (h * B + right) % M
        h = (h + M) % M  # Ensure non-negative
        hashes.append(h)

    return hashes
