from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = deque()
        for val in tokens:
            match val:
                case "*":
                    x = nums.pop()
                    y = nums.pop()
                    temp = x * y
                    nums.append(temp)
                case "/":
                    x = nums.pop()
                    y = nums.pop()
                    temp = int(y / x)
                    nums.append(temp)
                case "+":
                    x = nums.pop()
                    y = nums.pop()
                    temp = x + y
                    nums.append(temp)
                case "-":
                    x = nums.pop()
                    y = nums.pop()
                    temp = y - x
                    nums.append(temp)
                case _:  
                    nums.append(int(val))
                
        return nums.pop()