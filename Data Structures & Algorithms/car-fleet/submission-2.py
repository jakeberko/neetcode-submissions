import heapq

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        fleets = 1
        pairs = sorted(zip(position, speed), reverse=True)
            
        for pos, mph in pairs:
            time = (target - pos)/mph
            stack.append(time)
            if len(stack) >= 2:

                if stack[-1] > stack[-2]:
                    fleets +=1
                    stack.pop(-2)
                else:
                    stack.pop()
            
        return fleets
                
            
        return fleets
