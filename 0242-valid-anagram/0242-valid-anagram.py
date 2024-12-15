class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq_s = dict()
        freq_t = dict()

        for char_s, char_t in zip(s, t):
            freq_s[char_s] = freq_s.get(char_s, 0) + 1
            freq_t[char_t] = freq_t.get(char_t, 0) + 1
        
        return freq_s == freq_t