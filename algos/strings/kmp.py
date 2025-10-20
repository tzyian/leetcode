def prefix_function(s: str) -> list[int]:
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]  # reset j to the last matched prefix length
        # note this is done at the beginning of the loop
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j  # store the length of the longest prefix which is also a suffix

    return pi


def prefix2(s: str) -> list[int]:
    n = len(s)
    pi = [0] * n
    j = 0
    i = 1
    while i < n:
        if s[i] == s[j]:
            j += 1
            pi[i] = j
            i += 1
        elif j > 0:
            j = pi[j - 1]
        else:
            pi[i] = 0
            i += 1
    return pi


# This is shifted by 1 index i.e. different from the above two
def prefix3(s: str) -> list[int]:
    j = 0
    n = len(s)
    pi = [0] * (n + 1)

    for i in range(1, len(s)):
        if s[i] == s[j]:
            j += 1
            i += 1
            pi[i] = j
        else:
            i += 1 if j == 0 else 0
            j = pi[j]
    return pi


def string_matching(s: str, part: str) -> list[int]:
    ans = []
    n = len(s)
    m = len(part)

    lps = prefix_function(part)
    j = 0  # index for part
    for i in range(n):
        while j > 0 and s[i] != part[j]:
            j = lps[j - 1]
        if s[i] == part[j]:
            j += 1
        if j == m:
            ans.append(i - m + 1)  # store the starting index of the match
            j = lps[j - 1]
            # reset j to the last matched prefix length, finding new overlaps

    return ans


x = prefix_function("ababcababd")
y = prefix2("ababcababd")
z = prefix3("ababcababd")
print(x)
print(y)
print(z)
print(x == y)
