class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stk.append(char)
                print(stk)
            else:
                if len(stk) == 0: return False
                top = stk.pop()
                if char == ')' and top != '(': return False
                elif char == ']' and top != '[': return False
                elif char == '}' and top != '{': return False
                else: continue
        return len(stk) == 0