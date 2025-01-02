import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            m = (l+r)//2
            hrs_needed = sum([math.ceil(p/m) for p in piles])
            
            if hrs_needed <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        
        return res