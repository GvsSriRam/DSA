class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if not s or s[0] in ")}]":
            return False
        for c in s:
            if c == ")" and len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            elif c == "}" and len(stack) > 0 and stack[-1] == "{":
                stack.pop()
            elif c == "]" and len(stack) > 0 and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(c)

        return not stack