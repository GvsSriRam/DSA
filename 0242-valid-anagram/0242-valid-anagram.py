from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq_s = Counter(s)
        freq_t = Counter(t)

        for key, val in freq_s.items():
            if val != freq_t.get(key, 0):
                return False
        return True
        