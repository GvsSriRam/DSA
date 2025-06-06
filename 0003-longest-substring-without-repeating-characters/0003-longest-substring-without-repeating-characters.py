class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        last_idx = {}

        for r in range(len(s)):
            if s[r] in last_idx.keys():
                l = max(l, last_idx[s[r]]+1)
            last_idx[s[r]] = r
            res = max(res, r-l+1)
        return res
            
