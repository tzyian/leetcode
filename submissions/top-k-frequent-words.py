// https://leetcode.com/problems/top-k-frequent-words

from collections import Counter
from heapq import heapify, heappop
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ### most_common is in order of encountered ie not useful for duplicate keys
        # return [s for s, c in sorted(Counter(words).most_common(k), key=lambda x: (-x[1], x[0]))]
        c = Counter(words)
        heap = [(-cnt, word) for word, cnt in c.items()]
        heapify(heap)
        return [heappop(heap)[1] for _ in range(k)]
        