class MinStack:

    def __init__(self):
        self.stack = []
        self.min = -1

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.min = val
        else:
            self.min = min(self.min, val)
        self.stack.append((val, self.min))
    
    def pop(self) -> None:
        self.stack.pop()
        self.min = self.stack[-1][1]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.min