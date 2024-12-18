class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def valid(s: str):
            open_count = 0
            for c in s:
                open_count += 1 if c == "(" else -1

                if open_count < 0:
                    return False
            return not open_count
        
        def dfs(s: str):
            if 2*n == len(s):
                if valid(s):
                    res.append(s)
                return
            
            dfs(s+"(")
            dfs(s+")")
        
        dfs("")
        return res