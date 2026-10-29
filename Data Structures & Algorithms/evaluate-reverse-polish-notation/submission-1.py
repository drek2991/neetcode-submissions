class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        while len(tokens) >= 3:
            curr = int(tokens.pop(0))
            prev = int(tokens.pop(0))
            op = tokens.pop(0)
            if op == '+':
                val = curr+prev
                tokens.insert(0, val)
            elif op == '-':
                val = curr-prev
                tokens.insert(0, val)
            elif op == '*':
                val = curr*prev
                tokens.insert(0, val)
            elif op == '/':
                val = curr//prev
                tokens.insert(0, val)
            else:
                print("Error")
                return None
        return tokens[0]




