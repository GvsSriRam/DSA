class Solution:
    def is_valid_char(self, c: str) -> bool:
        if not c.isalnum():
            return False
        return True
    
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l<=r:
            while l < r and not self.is_valid_char(s[l]):
                l += 1
            
            while l < r and not self.is_valid_char(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
        return True