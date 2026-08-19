class MinStack:

    def __init__(self):
        self.minStack = []
        self.minStackSize = 0
        self.stack = []
        self.size = 0

    def push(self, val: int) -> None:
        if self.minStackSize == 0:
            self.minStack.append(val)
            self.minStackSize += 1
        elif val <= self.minStack[self.minStackSize - 1]:
            self.minStack.append(val)
            self.minStackSize += 1

        self.stack.append(val)
        self.size += 1
        return None

    def pop(self) -> None:
        val = self.stack[self.size - 1]
        del self.stack[self.size - 1]
        self.size -= 1
        if val == self.minStack[self.minStackSize - 1]:
            self.minStackSize -= 1
            del self.minStack[self.minStackSize]
            
        return None

    def top(self) -> int:
        return self.stack[self.size - 1]

    def getMin(self) -> int:
        return self.minStack[self.minStackSize - 1]
        
        
