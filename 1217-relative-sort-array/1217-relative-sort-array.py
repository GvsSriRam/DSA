class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        hashmap = {}

        for a in arr1:
            hashmap[a] = hashmap.get(a, 0) + 1
        
        for b in arr2:
            for _ in range(hashmap.pop(b, 0)):
                res.append(b)

        for a, v in sorted(hashmap.items()):
            for _ in range(v):
                res.append(a)
        
        return res
