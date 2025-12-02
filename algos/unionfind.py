UF = {}
size = dict()


def find(x: int) -> int:
    if x not in UF:
        UF[x] = x
        size[x] = 1
    if UF[x] != x:
        UF[x] = find(UF[x])
    return UF[x]


# amortised O(n)
def union(x: int, y: int) -> None:
    rootX = find(x)
    rootY = find(y)
    UF[rootX] = rootY


# amortised O(α(n))
def unionBySize(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX == rootY:
        return
    if size[rootX] < size[rootY]:
        UF[rootX] = rootY
        size[rootY] += size[rootX]
    else:
        UF[rootY] = rootX
        size[rootX] += size[rootY]
