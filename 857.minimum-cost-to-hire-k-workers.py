# @leet start

from heapq import heappush, heappushpop


class Solution:
    def mincostToHireWorkers(
        self, quality: list[int], wage: list[int], k: int
    ) -> float:
        wage_quality_ratio = [(q, w / q) for q, w in zip(quality, wage)]
        wage_quality_ratio.sort(key=lambda x: x[1])

        # a max-heap, so always pop the highest quality worker
        heap = []
        qual_sum = 0
        best = float("inf")
        for i, (q, _) in enumerate(wage_quality_ratio):
            if len(heap) < k - 1:
                heappush(heap, -q)
                qual_sum += q

            elif len(heap) == k - 1:
                heappush(heap, -q)
                qual_sum += q
                cost = wage_quality_ratio[i][1] * qual_sum
                best = cost

            elif len(heap) == k:
                q_lost = heappushpop(heap, -q)
                # + q_lost here because heap pops negative values
                qual_sum = qual_sum + q_lost + q
                cost = wage_quality_ratio[i][1] * qual_sum
                best = min(best, cost)
            else:
                raise Exception("heap should only be of size k")

        return best


# @leet end
