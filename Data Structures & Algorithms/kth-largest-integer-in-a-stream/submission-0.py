import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.num_heap = nums
        heapq.heapify(self.num_heap)
        while len(self.num_heap) > k:
            heapq.heappop(self.num_heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.num_heap, val)
        if len(self.num_heap) > self.k:
            heapq.heappop(self.num_heap)
        
        return self.num_heap[0]

        
