from collections.abc import MutableMapping
from dataclasses import dataclass, field
from typing import Iterator, Optional, override


@dataclass(eq=False)
class Node[K, V]:
    key: Optional[K] = None
    value: Optional[V] = None
    prev: Optional["Node[K, V]"] = field(default=None, repr=False)
    next: Optional["Node[K, V]"] = field(default=None, repr=False)


class LRUCache[K, V](MutableMapping[K, V]):
    """
    Cache with added statistics, and same interface as a standard dict.
    """

    def __init__(self, capacity: int) -> None:
        if capacity < 1:
            raise ValueError("Capacity must be >= 1")
        self.capacity = capacity

        self.head: Node[K, V] = Node()
        self.tail: Node[K, V] = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.values: dict[K, Node[K, V]] = {}

        self.hits: int = 0
        self.misses: int = 0
        self.evictions: int = 0

    @property
    def hit_rate(self) -> float:
        total = self.hits + self.misses
        return self.hits / total if total > 0 else 0.0

    @property
    def stats(self) -> dict[str, int | float]:
        return {
            "hits": self.hits,
            "misses": self.misses,
            "evictions": self.evictions,
            "hit_rate": self.hit_rate,
        }

    @override
    def __repr__(self) -> str:
        return f"LRUCache(capacity={self.capacity}, items={list(self.keys())}, stats={self.stats})"

    # --- MutableMapping Overrides ---
    @override
    def __getitem__(self, key: K) -> V:
        if key not in self.values:
            self.misses += 1
            raise KeyError(key)

        self.hits += 1
        node = self.values[key]
        self._move_to_front(node)
        return node.value

    @override
    def __setitem__(self, key: K, value: V) -> None:
        if key in self.values:
            node = self.values[key]
            node.value = value
            self._move_to_front(node)
        else:
            if len(self.values) >= self.capacity:
                self._evict()
            new_node = Node(key, value)
            self._add_to_head(new_node)
            self.values[key] = new_node

    @override
    def __delitem__(self, key: K) -> None:
        if key not in self.values:
            raise KeyError(key)
        node = self.values.pop(key)
        self._remove(node)

    @override
    def __iter__(self) -> Iterator[K]:
        curr = self.head.next
        while curr != self.tail:
            if curr:
                yield curr.key
                curr = curr.next

    @override
    def __len__(self) -> int:
        return len(self.values)

    @override
    def __contains__(self, key: object) -> bool:
        return key in self.values

    @override
    def __reversed__(self) -> Iterator[K]:
        curr = self.tail.prev
        while curr != self.head:
            if curr and curr.key is not None:
                yield curr.key
                curr = curr.prev

    @override
    def items(self) -> Iterator[tuple[K, V]]:
        curr = self.head.next
        while curr != self.tail:
            if curr and curr.key is not None:
                yield (curr.key, curr.value)
                curr = curr.next

    @override
    def values(self) -> Iterator[V]:
        curr = self.head.next
        while curr != self.tail:
            if curr:
                yield curr.value
                curr = curr.next

    @override
    def clear(self) -> None:
        self.head.next = self.tail
        self.tail.prev = self.head
        self.values.clear()
        self.hits = self.misses = self.evictions = 0

    @override
    def popitem(self) -> tuple[K, V]:
        if not self.values:
            raise KeyError("popitem(): cache is empty")
        lru_node = self.tail.prev
        key, val = lru_node.key, lru_node.value
        self._remove(lru_node)
        del self.values[key]
        return key, val

    @override
    def pop(self, key: K, default=None) -> V:
        if key not in self.values:
            if default is None:
                raise KeyError(key)
            return default
        node = self.values.pop(key)
        self._remove(node)
        return node.value

    @override
    def setdefault(self, key: K, default: V) -> V:
        if key in self.values:
            return self[key]
        self[key] = default
        return default

    # --- Internal Helpers ---
    def _evict(self) -> None:
        lru_node = self.tail.prev
        if lru_node and lru_node != self.head:
            self.evictions += 1
            if lru_node.key is not None:
                self._remove(lru_node)
                del self.values[lru_node.key]

    def _remove(self, node: Node[K, V]) -> None:
        if node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev

    def _add_to_head(self, node: Node[K, V]) -> None:
        first = self.head.next
        node.next = first
        node.prev = self.head
        self.head.next = node
        if first:
            first.prev = node

    def _move_to_front(self, node: Node[K, V]) -> None:
        self._remove(node)
        self._add_to_head(node)


if __name__ == "__main__":
    cache = LRUCache[int, str](capacity=2)
    cache["x"] = 100
    cache["y"] = 200
    cache["z"] = 300
    del cache["z"]
    print(list(cache.keys()))
    cache["x"] = 400
    cache["y"]
    ls = list(cache.items())
    print(ls)
    print(cache)
