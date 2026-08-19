import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone_heap = []
        for stone in stones:
            heapq.heappush(stone_heap, -stone)

        while len(stone_heap) > 1:
            y = -heapq.heappop(stone_heap)
            x = -heapq.heappop(stone_heap)

            if x != y:
                heapq.heappush(stone_heap, -(y-x))      
        
        if not stone_heap:
            return 0
        else:
            return -stone_heap[0]

