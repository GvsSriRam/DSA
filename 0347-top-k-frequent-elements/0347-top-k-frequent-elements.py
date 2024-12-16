class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        freqs = [[] for _ in range(len(nums)+1)]
        
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        for key, val in counts.items():
            freqs[val].append(key)
        
        res = []
        for idx in range(len(nums), 0, -1):
            for key in freqs[idx]:
                if len(res) != k:
                    res.append(key)
                else:
                    return res
        return res