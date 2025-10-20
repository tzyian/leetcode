def contains(text: str, pattern: str) -> bool:
    n, m = len(text), len(pattern)
    if m == 0 or m > n:
        return False

    BASE, MOD = 131, 10**9 + 7

    hpat = 0
    for ch in pattern:
        hpat = (hpat * BASE + ord(ch)) % MOD

    h = 0
    power = pow(BASE, m - 1, MOD)

    for i in range(n):
        left = ord(text[i - m])
        right = ord(text[i])

        h = (h * BASE + right) % MOD

        if i >= m:
            h = (h - left * power) % MOD

        if i >= m - 1 and h == hpat:
            if text[i - m + 1 : i + 1] == pattern:  # verify
                return True
    return False
