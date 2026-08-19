import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        remaining_stones=[]
        heapq.heapify(stones)

        while len(stones) != 2:
            val = heapq.heappop(stones)
            remaining_stones.append(val)
        
        x = heapq.heappop(stones)
        y = heapq.heappop(stones)

        if x != y:
            remaining_stones.append(y-x)
        
        if not remaining_stones:
            return 0

        return self.lastStoneWeight(remaining_stones)

