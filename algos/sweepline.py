from typing import List


def sweep_line(intervals: list[tuple[int, int]]) -> int:
    if not intervals:
        return 0

    events = []
    for s, e in intervals:
        events.append((s, 1))
        events.append((e, -1))

    events.sort(key=lambda x: (x[0], x[1]))

    curr = 0
    tot = 0
    for i in events:
        s, is_start = events[i]
        curr += is_start
        if curr > tot:
            tot = curr

    return tot


def corpFlightBookings(bookings: List[List[int]], n: int) -> List[int]:
    # 0-indexed
    # bookings = list[start, end, change]
    # start += change
    # end + 1 -= change

    # ([0] * n) + [0]

    arr = [0] * (n + 1)
    for s, e, upd in bookings:
        arr[s] += upd
        arr[e + 1] -= upd

    for i in range(1, n):
        arr[i] += arr[i - 1]

    return arr[:-1]
