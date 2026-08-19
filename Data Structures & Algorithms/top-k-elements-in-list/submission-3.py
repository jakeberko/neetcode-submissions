import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_freq = defaultdict(int)
        bucket = [[] for _ in range(len(nums)+1)]

        for num in nums:
            hash_freq[num] += 1
        
        for key, val in hash_freq.items():
            bucket[val].append(key)
        
        final = []
        for i in range(len(bucket) - 1, 0, -1):
            for val in bucket[i]:
                final.append(val)
                if len(final) == k:
                    return final

        