class MinStack:

    def __init__(self):
        self.minStack = []
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.minStack) == 0:
            self.minStack.append(val)
        elif val <= self.minStack[len(self.minStack) - 1]:
            self.minStack.append(val)

        self.stack.append(val)
        return None

    def pop(self) -> None:
        val = self.stack[len(self.stack) - 1]
        del self.stack[len(self.stack) - 1]
        if val == self.minStack[len(self.minStack) - 1]:
            del self.minStack[len(self.minStack) - 1]
            
        return None

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.minStack[len(self.minStack) - 1]
        
        
