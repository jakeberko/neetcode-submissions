from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemp, StackIdx = stack.pop()
                result[StackIdx] = i - StackIdx
            stack.append([t,i])

        return result


