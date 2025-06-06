import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq = Counter(nums)

        for key, val in freq.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)
        res = [heapq.heappop(heap)[1] for _ in range(k)]
        return res