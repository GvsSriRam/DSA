class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        res = []
        for key, val in sorted(counts.items(), key = lambda x: x[1], reverse=True):
            if len(res) == k:
                return res
            res.append(key)
        return res