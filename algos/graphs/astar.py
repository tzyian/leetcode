from heapq import heappush, heappop

Coord = tuple[int, int]


def astar(grid: list[list[int]]):
    R, C = len(grid), len(grid[0])
    start = (0, 0)
    gr, gc = R - 1, C - 1

    def h(r, c):  # Manhattan heuristic
        return abs(r - gr) + abs(c - gc)

    g: dict[Coord, int] = {start: 0}
    parent: dict[Coord, Coord | None] = {start: None}

    # f = g + h
    # g is distance, h is heuristic
    # open set as min-heap of (f, g, r, c)
    open_heap = []
    heappush(open_heap, (h(0, 0), 0, 0, 0))

    # consistent heuristic => closed set as visited
    closed = set()

    DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while open_heap:
        f, gcur, r, c = heappop(open_heap)
        if (r, c) in closed:
            continue
        if (r, c) == (gr, gc):
            path = []
            cur = (r, c)
            while cur is not None:
                path.append(cur)
                cur = parent[cur]
            path.reverse()
            return path, g[(gr, gc)]

        closed.add((r, c))

        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            if grid[nr][nc] == 1:
                continue

            tentative_g = g[(r, c)] + 1
            if (nr, nc) in g and tentative_g >= g[(nr, nc)]:
                continue

            g[(nr, nc)] = tentative_g
            parent[(nr, nc)] = (r, c)
            heappush(open_heap, (tentative_g + h(nr, nc), tentative_g, nr, nc))

    return None, None
