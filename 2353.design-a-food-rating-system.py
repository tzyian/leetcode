from typing import List

# @leet start
from collections import defaultdict
from heapq import heappush, heappop

INF = 10**9 + 7

# NOTE: don't break the heap invariant by mutating the rating in place without bubbling up/down


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # cmap[cuisine] = heap[(-rating, food)]
        # fmap[food] = (-rating, cuisine)

        self.cmap = defaultdict(list)
        self.fmap = dict()

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            heap = self.cmap[cuisine]
            heappush(heap, (-rating, food))

            self.fmap[food] = (-rating, cuisine)

    def changeRating(self, food: str, newRating: int) -> None:
        _, cuisine = self.fmap[food]
        self.fmap[food] = (-newRating, cuisine)
        heap = self.cmap[cuisine]
        heappush(heap, (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cmap[cuisine]
        while heap:
            neg_rating, food = heap[0]
            actual_rating, _ = self.fmap[food]
            if actual_rating == neg_rating:
                return food
            heappop(heap)
        return ""


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
# @leet end

calls = [
    "FoodRatings",
    "changeRating",
    "highestRated",
    "changeRating",
    "changeRating",
    "highestRated",
]
params = [
    [["a", "b", "c"], ["cuisine", "cuisine", "cuisine"], [11, 2, 15]],
    ["a", 12],
    ["cuisine"],
    ["c", 8],
    ["b", 5],
    ["cuisine"],
]

obj: None | FoodRatings = None
for call, arg in zip(calls, params):
    if call == "FoodRatings":
        obj = FoodRatings(*arg)
    elif call == "changeRating":
        assert obj is not None
        obj.changeRating(*arg)
    elif call == "highestRated":
        assert obj is not None
        result = obj.highestRated(*arg)
        print(result)

