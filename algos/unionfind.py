UF = {}


def union(x: int, y: int) -> None:
    rootX = find(x)
    rootY = find(y)
    UF[rootX] = rootY


def find(x: int) -> int:
    if x not in UF:
        UF[x] = x
    if UF[x] != x:
        UF[x] = find(UF[x])
    return UF[x]
