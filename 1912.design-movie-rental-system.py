# @leet imports start
from typing import *

# @leet imports end

# @leet start
from heapq import heappush, heappop, heapify

# NOTE: lol ignore this one, see the java.
# Lazy delete is annoying


class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        # entries: list of (shop, movie, price)

        # minheap of (price, movie, shop)
        self.unrented = [(price, movie, shop) for (shop, movie, price) in entries]
        heapify(self.unrented)

        # minheap of (price, shop, movie)
        self.rented = []

        # (shop, movie) = price. where +shop if not rented, -shop if rented
        self.entries = dict()

        for shop, movie, price in entries:
            self.entries[(shop, movie)] = price

    def search(self, movie: int) -> List[int]:
        res = []
        temp = []
        while self.unrented and len(res) < 5:
            price, m, shop = heappop(self.unrented)
            if m != movie or (shop, m) not in self.entries:
                temp.append((price, m, shop))
                continue
            res.append((price, m, shop))
        for x in res + temp:
            heappush(self.unrented, x)
        return [shop for (_, _, shop) in res]

    def rent(self, shop: int, movie: int) -> None:
        price = self.entries[(shop, movie)]
        del self.entries[(shop, movie)]
        self.entries[(-shop, movie)] = price
        heappush(self.rented, (price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.entries[(-shop, movie)]
        del self.entries[(-shop, movie)]
        self.entries[(shop, movie)] = price
        heappush(self.unrented, (price, movie, shop))

    def report(self) -> List[List[int]]:
        res = []
        temp = []
        while self.rented and len(res) < 5:
            price, shop, movie = heappop(self.rented)
            if (-shop, movie) not in self.entries:
                temp.append((price, shop, movie))
                continue
            res.append((price, shop, movie))
        for x in res + temp:
            heappush(self.rented, x)
        return [[shop, movie] for (_, shop, movie) in res]


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
# @leet end

