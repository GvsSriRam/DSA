import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        heap = []
        for num, freq in counts.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res