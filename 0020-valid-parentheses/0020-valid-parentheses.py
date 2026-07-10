class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {")": "(", "}": "{", "]": "["}
        stack = []
        
        for char in s:
            if char in lookup:
                top = stack.pop() if stack else '#'
                if lookup[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack
        